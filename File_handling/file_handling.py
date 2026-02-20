# Problems Without File Handling

# Data is lost after program ends

# If you store information in variables, it disappears as soon as the program stops.

# Example: A list of users entered during a session will vanish once the program closes.

# Sharing data between programs is difficult

# Without files, programs cannot easily exchange data with other applications or systems.

# No persistent storage for logs or history

# Applications like banking systems, websites, or games need to keep records permanently.

# Without files, there’s no way to save transaction history or user progress.

# Manual handling of structured data is cumbersome

# Saving data like tables (CSV), configuration (JSON), or multimedia requires manual entry every time.

# How File Handling Solves These Problems

# Persistent Storage

# Files allow data to persist on the disk, so it’s available even after the program ends.

# Example: Saving user registration details in a text file.

# Data Sharing Across Programs

# Files act as a bridge between applications. One program can write a file, another can read it.

# Logging and Record Keeping

# Programs can append data to logs, making it easy to track events or user actions.

# Structured and Efficient Data Management

# Using CSV, JSON, or binary files, programs can store complex data in a structured, machine-readable format.

# Automation and Backup

# Files can be copied, renamed, or moved automatically to create backups or transfer information.

# 1. What is File Handling?

# File handling allows a program to read, write, or manipulate files on a computer. Files can store data permanently, unlike variables which are temporary.

# Common file operations:

# Create a file

# Read a file

# Write to a file

# Append data

# Delete/rename files

# 2. File Modes in Python
# Mode	Meaning	Example Use
# 'r'	Read only	Reading configuration files
# 'w'	Write (overwrite)	Logging user input
# 'a'	Append	Adding new logs to existing file
# 'r+'	Read & write	Updating a file without deleting content
# 'b'	Binary mode	Reading images, PDFs, or Excel files
# 3. Basic File Operations
# 3.1 Creating and Writing to a File
# # Writing to a text file
# with open("file.txt", "w") as file:
#     file.write("Hello World!\n")
#     file.write("Python File Handling is easy topic.\n")

# Flushes Data to Disk
# When you write to a file, the operating system often stores data in a temporary buffer for efficiency.
# Closing the file ensures that all buffered data is actually written to the disk.
# If you don’t close it, some data may not be saved, causing data loss.

# Frees System Resources
# Files consume system resources (like file descriptors).
# Prevents Data Corruption
# Good Programming Practice


# ✅ Explanation:

# with open(...) as file: automatically closes the file after use.

# "w" mode overwrites the file if it exists.

# 3.2 Reading from a File
# # Reading from a file
# with open("file.txt", "r") as file:
#     content = file.read()
#     print(content)


# Output:

# Hello World!
# Python File Handling is easy.

# 3.3 Appending Data
# with open("file.txt", "a") as file:
#     file.write("Appending a new line.\n")

# 3.4 Reading Line by Line
# with open("file.txt", "r") as file:
#     for line in file:
#         print(line.strip())  # strip removes newline characters

# 4. Intermediate File Handling
# 4.1 Working with CSV Files
import csv

# Writing to CSV
# with open("data.csv", "w") as csvfile:
# with open("data.csv", "w", newline="") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["Name", "Age", "Country"])
#     writer.writerow(["Alice", 25, "USA"])
#     writer.writerow(["Bob", 30, "UK"])

# # Reading CSV
# with open("data.csv", "r") as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)


# Real-world use case: Storing user details, exporting reports.

# 4.2 JSON Files
import json
# from json import dump
# Writing JSON
# data = {"name": "Alice", "age": 25, "city": "New York"}
# with open("data.json", "w") as json_file:
#     json.dump(data, json_file)

# # Reading JSON
# with open("data.json", "r") as json_file:
#     data_loaded = json.load(json_file)
#     print(data_loaded)

# Appending to JSON
import json
new_data = {"name": "Bob", "age": 30, "city": "London"}

# # Step 1: Read existing data
with open("data.json", "r") as file:
    existing_data = json.load(file)

# Step 2: Convert to list if it's a dict
if isinstance(existing_data, dict):
    existing_data = [existing_data]

# Step 3: Append new data
existing_data.append(new_data)

# Step 4: Write back
with open("data.json", "w") as file:
    json.dump(existing_data, file, indent=4)

# Use Case: APIs, configuration files, storing structured data.

# 5. Advanced File Handling
# 5.1 Binary Files (Images, PDFs)

# Reading a binary file (image)
# with open("image.png", "rb") as img_file:
#     data = img_file.read()
#     print(f"Image size: {len(data)} bytes")

# # Writing binary data
# with open("copy_image.png", "wb") as img_file:
#     img_file.write(data)


# Use Case: File backup, image processing, multimedia apps.

# 5.2 File Handling with Exception Handling
# try:
#     with open("non_existent.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found! Please check the file path.")

# 5.3 Using os and shutil for File Operations
# import os
# import shutil

# # Rename a file
# os.rename("example.txt", "example_renamed.txt")

# # Copy a file
# shutil.copy("example_renamed.txt", "backup_example.txt")

# # Delete a file
# os.remove("backup_example.txt")


# Real-world use case: File management systems, automated backups.

# 5.4 Reading Large Files Efficiently
# with open("large_file.txt", "r") as file:
#     for line in file:
#         process(line)  # hypothetical function to handle line


# ✅ Avoids loading the entire file into memory.

# 6. Real-World Use Cases of File Handling

# Log Management: Storing application logs for debugging.

# Data Storage: Saving user data in CSV/JSON for apps.

# Configuration Files: Reading .ini or .json for app settings.

# Media Handling: Processing images, videos, or PDFs.

# Backup & Restore: Automatically copy, rename, and archive files.

# Web Scraping: Saving scraped data to files for analysis.