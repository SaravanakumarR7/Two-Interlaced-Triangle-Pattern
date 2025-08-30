# Two-Interlaced-Triangle-Pattern

Interlaced Star and Hash Triangle Pattern:

    This Python program generates a visually interlaced pattern of two triangles using stars (*) and hashes (#). The pattern consists of:
    
    Inverted triangle (*) — the “star” triangle pointing downward
    
    Upright triangle (#) — the “hash” triangle pointing upward
    
    Indentation represented by - for empty spaces
    
    The triangles are interlaced in the same rows without overlapping incorrectly. The pattern dynamically adjusts based on the user-provided heights for the star and hash triangles.

Features:

    Dynamically handles any size of star and hash triangles.
    
    Calculates indentation and spacing automatically.
    
    Ensures * does not overwrite # in the interlaced rows.
    
    Produces a clean and readable pattern in the console.

How It Works:

    Initializes a 2D list with spaces to store the pattern.
    
    Fills the upright hash triangle (#) first, computing proper indentation for each row.
    
    Overlays the inverted star triangle (*), taking care not to overwrite existing # symbols.
    
    Joins each row and prints the final interlaced pattern.
