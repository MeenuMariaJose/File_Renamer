import os
import tempfile
import pytest
import sys
import file_rename
import io

# Test cases for the renaming function
# with delete=False ensures that the temporary file is not automatically deleted when it's closed
def test_fun_rename():
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b"Test content") #This writes the string "Test content" encoded as bytes to the temporary file.
        temp_file_path = temp_file.name
    
    new_name = file_rename.fun_rename(temp_file_path, "_keyword")
    assert os.path.exists(new_name)
    assert "_keyword" in new_name  # Modify the assertion

# Test cases for the main functionality
@pytest.mark.parametrize("args", [
    (["-f", "file.txt", "-s", "_keyword"]),
    (["-d", "directory", "-s", "_keyword"]),
])
def test_main_functionality(args):
    sys.argv[1:] = args  # Exclude the first argument which is the script name
    #This also, simulating command-line arguments passed to the script
    captured_stdout = io.StringIO() #This creates a StringIO object, which can capture the standard output.
    sys.stdout = captured_stdout
    
    # Create the file or directory if it doesn't exist
    if args[0] == "-f":
        with open("file.txt", "w") as f:
            f.write("Test content")
    else:
        if not os.path.exists("directory"):  # Check if directory already exists
            os.makedirs("directory")
    
    file_rename.main()
    captured_output = captured_stdout.getvalue()

    if args[0] == "-f":
        assert "New file name is:" in captured_output
        assert "All files in directory renamed with the keyword." not in captured_output
    else:
        assert "All files in directory renamed with the keyword." in captured_output
        assert "New file name is:" not in captured_output
