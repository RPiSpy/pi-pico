#--------------------------------------
#    ___  ___  _ ____          
#   / _ \/ _ \(_) __/__  __ __ 
#  / , _/ ___/ /\ \/ _ \/ // / 
# /_/|_/_/  /_/___/ .__/\_, /  
#                /_/   /___/   
#
#  ST7567S LCD 128x64 Screen
#
#  Library
#
# Author : Matt Hawkins
# Date   : 28/11/2024
#
# https://www.raspberrypi-spy.co.uk/
#
# The MIT License (MIT)
# Copyright 2024 Matt Hawkins
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#--------------------------------------

from machine import I2C, Pin
import time

class st7567s:
    
    # LCD Command and Data Flags
    LCD_CMD = 0x00  # Command mode
    LCD_DATA = 0x40  # Data mode

    # Common commands used in functions
    CMD_DISPLAY_OFF=0xAE              # Turn display ON
    CMD_DISPLAY_ON=0xAF               # Turn display OFF
    CMD_ALL_PIXELS_OFF=0xA4           # Turn all pixels OFF
    CMD_ALL_PIXELS_ON=0xA5            # Turn all pixels ON
    CMD_NORMAL=0xA6                   # Normal display (not inverted)
    CMD_INVERT=0xA7                   # Inverted display (pixels are reversed).

    # Initial offset used during rotation
    LCD_DRAM_OFFSET=0x00

    def __init__(self, scl_pin, sda_pin, addr=0x3f):
        
        # Define local variables. Width and Height hardcoded
        # because the ST7567 doesn't support any other sizes.
        self.addr = addr
        self.width = 128
        self.height = 64
        self.i2c = I2C(0, scl=Pin(scl_pin), sda=Pin(sda_pin), freq=400000)
        self.buffer = bytearray(self.width * (self.height // 8))  # Screen buffer (1 byte per row of 8 vertical pixels)

    # Initialize the LCD
    def init(self):
        """Initialize the ST7567 LCD."""
        self.send_command(0xE2)  # Software reset
        self.send_command(0xA0)  # Segment direction - Normal (A0); Reverse (A1)
        self.send_command(0xC8)  # Common output scan direction - Normal (C0); Reverse (C8)
        self.send_command(0x27)  # Adjust as required (0x20–0x27)
        self.send_command(0x2F)  # Power control set - Booster, Regulator, and Follower ON
        self.send_command(0xA6)  # Normal display - Normal (A6); Reverse (A7)
        self.send_command(0xA4)  # Normal (A4); Entire display ON (A5)
        self.send_command(0xA2)  # LCD bias set - Bias 1/9 (A2); Bias 1/7 (A3)
        self.send_command(0x10)  # Upper nibble of column address
        self.send_command(0x00)  # Lower nibble of column address
        self.send_command(0x40)  # Set display start line 0
        self.send_command(0xB0)  # Set page address 0
        self.send_command(0xAF)  # Display on

    # Send command with retry
    def send_command(self, cmd):
        """Send a command byte to the LCD."""
        retrycount=0
        errors=0
        while (retrycount<3 and errors==0):
            try:
                self.i2c.writeto(self.addr, bytes([self.LCD_CMD, cmd]))
                errors=1
            except:
                print("  Error sending command. Retry ...")
                retrycount=retrycount+1
                errors=0

    # Send data with retry
    def send_data(self, data):
        """Send data bytes to the LCD."""
        retrycount=0
        errors=0
        while (retrycount<3 and errors==0):
            try:
                self.i2c.writeto(self.addr, bytes([self.LCD_DATA]) + bytes(data))
                errors=1
            except:
                print("  Error sending data. Retry ...")
                retrycount=retrycount+1
                errors=0

    # Set contrast
    def set_contrast(self, level):
        """
        Set the contrast level of the ST7567 LCD.
        :param level: Contrast level (0-63).
        """
        if not (0 <= level <= 63):
            raise ValueError("Contrast level must be between 0 and 63.")
        
        self.send_command(0x81)  # Contrast control mode
        self.send_command(level)  # Set contrast level (0-63)
    
    # Clear the display
    def clear(self):
        """Clear the entire LCD screen."""
        for i in range(len(self.buffer)):
            self.buffer[i] = 0
        self.update_screen()

    # Set a pixel
    def set_pixel(self, x, y, color):
        """
        Sets a single pixel in the buffer.

        Args:
            x (int): X-coordinate of the pixel.
            y (int): Y-coordinate of the pixel.
            color (int): 1 for pixel on, 0 for pixel off.
        """
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return  # Ignore out-of-bounds pixels

        # Determine the byte and bit position in the buffer
        byte_index = x + (y // 8) * self.width
        bit = y % 8

        if color:
            self.buffer[byte_index] |= (1 << bit)  # Turn the bit on
        else:
            self.buffer[byte_index] &= ~(1 << bit)  # Turn the bit off
         
    # Draw rectangle
    def draw_rectangle(self, x, y, width, height, color):
        """
        Draws a rectangle on the screen.

        Args:
            x (int): X-coordinate of the top-left corner.
            y (int): Y-coordinate of the top-left corner.
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            color (int): 1 for pixel on, 0 for pixel off.
        """
        # Draw horizontal lines
        for i in range(x, x + width):
            self.set_pixel(i, y, color)               # Top edge
            self.set_pixel(i, y + height - 1, color) # Bottom edge

        # Draw vertical lines
        for i in range(y, y + height):
            self.set_pixel(x, i, color)              # Left edge
            self.set_pixel(x + width - 1, i, color)  # Right edge

    # Draw filled rectangle
    def fill_rectangle(self, x, y, width, height, color):
        """
        Draws a filled rectangle on the screen.

        Args:
            x (int): X-coordinate of the top-left corner.
            y (int): Y-coordinate of the top-left corner.
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            color (int): 1 for pixel on, 0 for pixel off.
        """
        for i in range(y, y + height):
            for j in range(x, x + width):
                self.set_pixel(j, i, color)

    # Draw circle
    def draw_circle(self, cx, cy, radius, color):
        """
        Draws a circle using the midpoint circle algorithm.

        Args:
            cx (int): X-coordinate of the circle center.
            cy (int): Y-coordinate of the circle center.
            radius (int): Radius of the circle.
            color (int): 1 for pixel on, 0 for pixel off.
        """
        x = radius
        y = 0
        err = 0

        while x >= y:
            # Draw points for each octant
            self.set_pixel(cx + x, cy + y, color)
            self.set_pixel(cx + y, cy + x, color)
            self.set_pixel(cx - y, cy + x, color)
            self.set_pixel(cx - x, cy + y, color)
            self.set_pixel(cx - x, cy - y, color)
            self.set_pixel(cx - y, cy - x, color)
            self.set_pixel(cx + y, cy - x, color)
            self.set_pixel(cx + x, cy - y, color)

            y += 1
            err += 1 + 2 * y
            if 2 * (err - x) + 1 > 0:
                x -= 1
                err += 1 - 2 * x

    # Draw filled circle
    def fill_circle(self, cx, cy, radius, color):
        """
        Draws a filled circle.

        Args:
            cx (int): X-coordinate of the circle center.
            cy (int): Y-coordinate of the circle center.
            radius (int): Radius of the circle.
            color (int): 1 for pixel on, 0 for pixel off.
        """
        for y in range(-radius, radius + 1):
            for x in range(-radius, radius + 1):
                if x*x + y*y <= radius*radius:
                    self.set_pixel(cx + x, cy + y, color)

    # Draw character
    def draw_char(self, x, y, char, font, color):
        """
        Draws a single character from the provided font array on the screen.

        Args:
            x (int): X-coordinate of the character's top-left corner.
            y (int): Y-coordinate of the character's top-left corner.
            char (str): The character to draw.
            color (int): 1 for pixel on, 0 for pixel off.
        """
        # Ensure the character is in the FONT_5X8 dictionary
        if char not in font:
            return  # Ignore undefined characters

        char_data = font[char]  # Retrieve the font data (5 bytes per character)
        for col, byte in enumerate(char_data):  # Iterate through each column of the character
            for row in range(8):  # Each byte is 8 bits high
                if byte & (1 << row):  # Check if the bit is set
                    self.set_pixel(x + col, y + row, color)  # Draw pixel

        # Optional: Add a 1-pixel spacing between characters
        for row in range(8):
            self.set_pixel(x + len(char_data), y + row, 0)  # Clear space after character

    # Draw a scaled character
    def draw_scaled_char(self, x, y, char, font, scale, color):
        """
        Draws a scaled character from a smaller font.

        Args:
            x (int): X-coordinate.
            y (int): Y-coordinate.
            char (str): Character to draw.
            font (dict): Font dictionary.
            scale (int): Scale factor (e.g., 2 for 2x size).
            color (int): 1 for pixel ON, 0 for pixel OFF.
        """
        # Ensure the character is in the FONT_5X8 dictionary
        if char not in font:
            return  # Ignore undefined characters

        char_data = font[char]
        for row in range(8):  # Original font height
            for col in range(5):  # Original font width
                if char_data[col] & (1 << row):
                    # Draw scaled pixels
                    for sx in range(scale):
                        for sy in range(scale):
                            self.set_pixel(x + col * scale + sx, y + row * scale + sy, color)

    # Draw a text string
    def draw_text(self, x, y, text, font, scale, color):
        """
        Draws a string of text on the screen.

        Args:
            x (int): X-coordinate of the text's starting position.
            y (int): Y-coordinate of the text's starting position.
            text (str): The string to draw.
            font (dict): Font dictionary.
            scale (int): Scale factor (e.g., 2 for 2x size).
            color (int): 1 for pixel on, 0 for pixel off.
        """
        for i, char in enumerate(text):
            if (scale==1):
                self.draw_char(x + i * 6, y, char, font, color)  # Characters are 5 pixels wide + 1 pixel spacing
            else:
                self.draw_scaled_char(x + i * (6*scale), y, char, font, scale, color)  # Characters are 5 pixels wide + 1 pixel spacing

    # Draw a bitmap
    def draw_bitmap(self, x, y, width, height, bitmap, color):
        """
        Draws a bitmap image to the screen.

        Args:
            x (int): X-coordinate of the top-left corner of the image.
            y (int): Y-coordinate of the top-left corner of the image.
            width (int): Width of the bitmap in pixels.
            height (int): Height of the bitmap in pixels.
            bitmap (list): A list of bytes representing the bitmap.
            color (int): 1 for pixel on, 0 for pixel off.
        """
        for i in range(height):  # Iterate through each row
            for j in range(width):  # Iterate through each column
                byte_index = i * ((width + 7) // 8) + (j // 8)
                bit_index = 7 - (j % 8)
                if byte_index < len(bitmap) and (bitmap[byte_index] & (1 << bit_index)):
                    self.set_pixel(x + j, y + i, color)

    def draw_bmp_file(self, filename, x_offset=0, y_offset=0, invert=False):
        """
        Draws a monochrome BMP image from a file to the screen.

        Args:
            filename (str): Path to the BMP file.
            x_offset (int): X-coordinate offset for displaying the image.
            y_offset (int): Y-coordinate offset for displaying the image.
            invert (bool): If True, inverts the colors (black becomes white and vice versa).
        """
        with open(filename, 'rb') as f:
            # Read BMP header (14 bytes)
            f.seek(10)  # Offset to pixel data
            pixel_data_offset = int.from_bytes(f.read(4), 'little')
            
            # Read DIB header
            f.seek(18)  # Width and height offsets
            width = int.from_bytes(f.read(4), 'little')
            height = int.from_bytes(f.read(4), 'little')
            
            f.seek(28)  # Bit depth offset
            bit_depth = int.from_bytes(f.read(2), 'little')
            if bit_depth != 1:
                raise ValueError("Only monochrome BMP files (1-bit depth) are supported.")
            
            # Calculate row size (padded to a multiple of 4 bytes)
            row_size = ((width + 31) // 32) * 4
            
            # Move to the pixel data
            f.seek(pixel_data_offset)
            
            # Read and render the pixel data
            for y in range(height):
                row_data = f.read(row_size)
                for x in range(width):
                    byte_index = x // 8
                    bit_index = 7 - (x % 8)
                    pixel = (row_data[byte_index] >> bit_index) & 1
                    
                    # Apply inversion if requested
                    if invert:
                        pixel = 1 - pixel
                    
                    # Set pixel on the display (BMP origin is bottom-left)
                    self.set_pixel(x + x_offset, y_offset + (height - 1 - y), pixel)


    def draw_pbm_file(self, filename, x_offset=0, y_offset=0, invert=False):
        """
        Draws a monochrome bitmap image from a file to the screen.

        Args:
            filename (str): Path to the bitmap file.
            x_offset (int): X-coordinate offset for displaying the image.
            y_offset (int): Y-coordinate offset for displaying the image.
            invert (bool): If True, inverts the colors (black becomes white and vice versa).
        """
        with open(filename, "rb") as f:
            # Example assumes a custom file format or monochrome PBM (P4).
            # Read the header (adjust based on your file's format).
            header = f.readline().decode().strip()
            if header not in ('P1', 'P4'):
                raise ValueError("Unsupported format: Only P1 (ASCII) and P4 (Binary) PBM files are supported.")

            # Skip comments in the PBM file
            while True:
                line = f.readline().decode().strip()
                if not line.startswith('#'):
                    width, height = map(int, line.split())
                    break

            # Read pixel data
            if header == 'P1':
                # ASCII PBM (P1): Read as plain 0s and 1s
                pixel_data = []
                for line in f:
                    pixel_data.extend(int(bit) for bit in line.decode().split())
            elif header == 'P4':
                # Binary PBM (P4): Read binary data directly
                pixel_data = list(f.read())

            # Render the bitmap
            for y in range(height):
                for x in range(width):
                    if header == 'P1':
                        # Each pixel is either 0 or 1
                        pixel = pixel_data[y * width + x]
                    elif header == 'P4':
                        # Each byte contains 8 pixels (MSB first)
                        byte_index = (y * width + x) // 8
                        bit_index = 7 - (x % 8)
                        pixel = (pixel_data[byte_index] >> bit_index) & 1
                    
                    # Apply inversion if requested
                    if invert:
                        pixel = 1 - pixel
                    
                    # Draw the pixel
                    self.set_pixel(x + x_offset, y + y_offset, pixel)

    # Draw a line
    def draw_line(self, x0, y0, x1, y1, color):
        """
        Draws a straight line on the screen using Bresenham's line algorithm.

        Args:
            x0 (int): Starting x-coordinate.
            y0 (int): Starting y-coordinate.
            x1 (int): Ending x-coordinate.
            y1 (int): Ending y-coordinate.
            color (int): 1 for pixel ON, 0 for pixel OFF.
        """
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy

        while True:
            self.set_pixel(x0, y0, color)  # Set the pixel at the current point

            if x0 == x1 and y0 == y1:
                break
            
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy


    # Update screen using current buffer
    def update_screen(self):
        """
        Writes the buffer to the display.
        """
        for page in range(self.height // 8):         # Iterate through each page
            self.send_command(0xB0 | page)           # Set page address
            self.send_command(self.LCD_DRAM_OFFSET)  # Set lower column address
            self.send_command(0x10)                  # Set higher column address
            self.send_data(self.buffer[page * self.width:(page + 1) * self.width])

    # Set screen mode
    def mode(self, enable):
        """ Invert the pixels """       
        if (enable==0):
            self.send_command(self.CMD_NORMAL)  # Normal
        elif (enable==1):
            self.send_command(self.CMD_INVERT)  # Invert
        else:
            self.send_command(self.CMD_NORMAL)  # Normal

    # Enable or Disable screen
    def display(self, enable):
        """ Turn display on or off """
        if (enable==1):
            self.send_command(self.CMD_DISPLAY_ON)  # Display ON
        elif (enable==0):
            self.send_command(self.CMD_DISPLAY_OFF) # Display OFF
        else:
            self.send_command(self.CMD_DISPLAY_ON)

    # Rotate screen 0 or 180 degrees
    def rotate_display(self, rotated):
        if rotated:
            self.send_command(0xA1)  # Reverse column direction
            self.send_command(0xC0)  # Reverse row direction
            self.LCD_DRAM_OFFSET=0x04
        else:
            self.send_command(0xA0)  # Normal column direction
            self.send_command(0xC8)  # Normal row direction
            self.LCD_DRAM_OFFSET=0x00
        self.update_screen()
