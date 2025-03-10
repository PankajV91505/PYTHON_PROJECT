import os  
import shutil  

# Step 1: Define folder categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Executables": [".exe", ".msi"],
    "Others": []  # Files that don’t match any category
}

# # Step 2: Get the directory path from the user
# def organize_files(directory):
#     if not os.path.exists(directory):  
#         print("Invalid directory! Please enter a valid path.")
#         return

#     # Step 3: Loop through all files in the directory
#     for filename in os.listdir(directory):
#         file_path = os.path.join(directory, filename)

#         # Skip directories (we only want to move files)
#         if os.path.isdir(file_path):
#             continue  

#         # Step 4: Identify file extension
#         file_extension = os.path.splitext(filename)[1].lower()  

#         # Step 5: Determine file category
#         category_found = False
#         for category, extensions in FILE_CATEGORIES.items():
#             if file_extension in extensions:
#                 move_file(directory, filename, category)
#                 category_found = True
#                 break

#         # Step 6: Move uncategorized files to "Others"
#         if not category_found:
#             move_file(directory, filename, "Others")

# # Step 7: Function to move files to categorized folders
# def move_file(directory, filename, category):
#     category_path = os.path.join(directory, category)

#     # Create category folder if it doesn’t exist
#     if not os.path.exists(category_path):
#         os.makedirs(category_path)

#     # Move the file to the appropriate folder
#     shutil.move(os.path.join(directory, filename), os.path.join(category_path, filename))
#     print(f"Moved: {filename} --> {category}/")

# # Step 8: Run the script
# if __name__ == "__main__":
#     folder_path = input("Enter the folder path to organize: ")
#     organize_files(folder_path)
#     print("✅ File organization complete!")
