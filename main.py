from models.menu import Menu
from models.converter import Converter
from models.system import System

menu = Menu()
convert = Converter()
sys = System()

if __name__ == "__main__":

    # SELECT FOLDER AND COLLECT FILE PATHS INTO A DICT
    input_path = menu.select_folder("Select folder with audios to convert!")
    fileList = menu.get_files(input_path)
    
    # SELECT FOLDER TO SAVE ALL CONVERTED AUDIOS
    output_path = menu.select_folder("Select folder to save converted audios!")

    info_json = {
        "input_path": input_path,
        "fileList": fileList,
        "output_path": output_path
    }

    # CONVERT AUDIOS
    convert.execute(fileList, output_path)
    menu.alert("Audios Converted!\nClick OK to finish program.")
    sys.exit()

