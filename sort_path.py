import sys
import shutil
from pathlib import Path
from constants import RED, BLUE, YELLOW, CYAN, GRAY, WHITE, RESET


CATEGORIES = {
    "Archives": [".zip", ".gz", ".tar"],
    "Audio": [".mp3", ".wav", ".flac", ".wma", ".ogg"],
    "Video": [".avi", ".mp4", ".mov", ".mkv"],
    "Images": [".jpeg", ".png", ".jpg", ".svg", ".gif"],
    "Documents": [".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx"],
    "Python": [
        ".py",
        ".rpy",
        ".pyw",
        ".cpy",
        ".gyp",
        ".gypi",
        ".pui",
        ".ipy",
        ".pyt",
        ".whl",
    ],
    "Other": [],
}

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = (
    "a",
    "b",
    "v",
    "g",
    "d",
    "e",
    "jo",
    "zh",
    "z",
    "y",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "r",
    "s",
    "t",
    "u",
    "f",
    "h",
    "ts",
    "ch",
    "sh",
    "sch",
    "`",
    "y",
    "'",
    "e",
    "yu",
    "ya",
    "je",
    "i",
    "ji",
    "g",
)
TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[c] = l
    TRANS[c.upper()] = l.upper()


def normalize(file_name: str) -> str:  # +++
    name = str(Path(file_name).stem)
    result = ""
    for i in range(len(name)):
        if "0" <= name[i] <= "9" or "a" <= name[i] <= "z" or "A" <= name[i] <= "Z":
            result += name[i]
        elif name[i] in TRANS:  # cyrylic
            result += TRANS[name[i]]
        else:
            result += "_"
    return result + str(Path(file_name).suffix)


def archive_unpack(dir: Path) -> None:  # +++ ?list(CATEGORIES.keys())[0]
    category_arc = list(CATEGORIES.keys())[0]
    # "Archives" must be first in the list (dict CATEGORIES) !!!
    path_arc = dir.joinpath(category_arc)
    if path_arc.exists():
        for element_file in path_arc.glob("*"):
            if (
                element_file.is_file()
                and str(element_file.suffix) in list(CATEGORIES.values())[0]
            ):
                print(f"Unpacking: {element_file.name} ...")
                shutil.unpack_archive(
                    element_file, path_arc.joinpath(element_file.stem)
                )


def del_empty_tree(path: Path) -> None:  # +++
    for element in path.glob("**/*"):
        if element.is_dir() and element.stem not in CATEGORIES:
            shutil.rmtree(element)


def get_categories(file: Path) -> str:  # +++
    ext = file.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            return cat
    return "Other"


def move_file(file: Path, category: str, root_dir: Path, is_replace) -> None:  # +++
    target_dir = root_dir.joinpath(category)
    if not target_dir.exists():
        target_dir.mkdir()
    new_path = target_dir.joinpath(normalize(file.name))

    if new_path.exists() and new_path != file and not is_replace:
        while new_path.exists():
            new_path = new_path.with_stem(new_path.stem + "_")
    file.replace(new_path)


def sort_folder(path: Path, is_replace) -> None:  # +++
    for element in path.glob("**/*"):
        if element.is_file():
            category = get_categories(element)
            move_file(element, category, path, is_replace)


def list_print_and_write(text: str, is_echo: bool, file_dscr):  # +++
    file_dscr.write(text + "\n")  # to file
    if is_echo:
        print(text)  # to screen (only main dir)


def list_files_write(
    el_path: Path, echo_list=False
) -> None:  # +++ ?"{:>3}".format(count)
    FILE_LIST_TITLE = f"{YELLOW}\t_ List Of Files: _{RESET}"
    file_list = el_path.joinpath("_file_list_.txt")
    count = 0

    with open(file_list, "w") as file_out:
        list_print_and_write(FILE_LIST_TITLE, echo_list, file_out)
        for element in el_path.glob("**/*"):
            if element.is_file() and element != file_list:
                count += 1
                list_print_and_write(
                    GRAY + "{:>3}".format(count) + f"{WHITE}. {str(element)[len(str(el_path))+1:]}{RESET}",
                    echo_list,
                    file_out,
                )


def list_files(path: Path) -> None:  # +++
    list_files_write(path, True)  # for main dir
    for element_path in path.iterdir():  # for iterdirs
        if element_path.is_dir():
            list_files_write(element_path)


"""================= для отладки ================="""


def prepare_folder() -> None:
    TEST_FOLDER = "D:\\000"
    SOURS_FOLDER = "D:\\000_Original"
    shutil.rmtree(TEST_FOLDER, ignore_errors=True)
    p = input("press any key >>> ")  # пауза
    shutil.copytree(SOURS_FOLDER, TEST_FOLDER)
    p = input("press any key >>> ")  # пауза


"""================= для отладки ================="""


# def main() -> str:
def sorting(*args) -> str:
    # print(f"{args = }")
    try:
        path = Path(args[0])
    except IndexError:
        return f"   {RED}no path to folder{RESET}"

    if not path.exists():
        return f"   {RED}folder {RESET}'{args[0]}'{RED} does not exist{RESET}"

    try:
        is_replace = sys.argv[2]
    except IndexError:
        is_replace = False

    # prepare_folder()  # прибрати - це для отладки

    sort_folder(path, is_replace)
    del_empty_tree(path)
    list_files(path)
    archive_unpack(
        path
    )  # щоб файли з архівів теж були у списку, перенести цю строку вище

    return f"{YELLOW}\n*** Completed Successfully ***\n{RESET}"


if __name__ == "__main__":
    print(sorting("d:\\000"))
    # print(sorting("d:\\00"))
    # print(sorting())
