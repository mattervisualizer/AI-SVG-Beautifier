import sys
import os
import re
import time
import xml.dom.minidom

class Script():
    def __init__(self):
        pass

    def _remove_xml_tag_and_generator_info(self, path):
        for filename in os.listdir(path):
            if filename.endswith(".svg"):
                file_path = os.path.join(path, filename)
                try:
                    with open(file_path, "r") as f:
                        svg_content = f.read()
                    svg_lines = svg_content.splitlines()
                    svg_lines = [line for line in svg_lines if not line.startswith("<?xml") and not line.startswith("<!-- Generator")]
                    with open(file_path, "w") as f:
                        f.write('\n'.join(svg_lines))
                    print(f"[!] XML tag and generator information removed from {filename}")
                except Exception as e:
                    print(f"[!] File {filename} wasn't modified due to {str(e)}")

    def _replace_fills_by_currentcolor(self, path):
        for filename in os.listdir(path):
            if filename.endswith(".svg"):
                file_path = os.path.join(path, filename)
                try:
                    doc = xml.dom.minidom.parse(file_path)
                    style_tags = doc.getElementsByTagName('style')
                    for style_tag in style_tags:
                        style_content = style_tag.firstChild.data
                        style_content = re.sub(r'#([0-9A-Fa-f]{6})', r'currentColor', style_content)
                        style_tag.firstChild.replaceWholeText(style_content)
                    xml_content = doc.toprettyxml(indent="  ")
                    xml_content = "\n".join([line for line in xml_content.split("\n") if line.strip()])
                    with open(file_path, 'w') as f:
                        f.write(xml_content)
                    print(f"[!] Fills in {filename} replaced with 'currentColor' tag")
                except Exception as e:
                    print(f"[!] File {filename} wasn't modified due to {str(e)}")

    def _make_one_line(self, path):
        for filename in os.listdir(path):
            if filename.endswith(".svg"):
                file_path = os.path.join(path, filename)
                try:
                    with open(file_path, "r") as f:
                        svg_content = f.read()
                    dom = xml.dom.minidom.parseString(svg_content)
                    svg_one_line = dom.toxml().replace("\n", "").replace("\t", "").replace("\r", "")
                    svg_one_line = ' '.join(svg_one_line.split())
                    with open(file_path, "w") as f:
                        f.write(svg_one_line)
                    print(f"[!] File {filename} modified into a single line")
                except Exception as e:
                    print(f"[!] File {filename} wasn't modified due to {str(e)}")

    def _restarter(self):
        print("[.] Restarting in 3 seconds...")
        time.sleep(3)
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def _cleaner(self):
        match os.name:
            case "posix":
                os.system("clear")
            case "nt":
                os.system("cls")
            case _:
                print("[!] Unable to clear the screen. Unsupported operating system")
                self._restarter()

    def _yornchecker(self, inp):
        match inp:
            case "y":
                pass
            case "n":
                pass
            case _:
                print("[!] Invalid Input")
                self._restarter()

    def _pathchecker(self, path):
        if not os.path.exists(path):
            print("[!] Invalid path")
            self._restarter()
        files = os.listdir(path)
        svg_files = [file for file in files if file.endswith(".svg")]
        if svg_files:
            print(f"[>] This files will be modified: ")
            for svg_file in svg_files:
                print(f"- {svg_file}")
        else:
            print("[!] Folder does not contain any svg file. Try again")
            self._restarter()

    def _usrinput(self):
        self._cleaner()

        usr_path: str = input("[>] Insert the path with your SVG icons that you drew in Adobe Illustrator: ")
        self._pathchecker(usr_path)

        usr_replace_fiils_by_currentcolor: str = input("[>] Do you want to remove all fills and replace it with 'currentColor' tag? [y/n]: ").lower()
        self._yornchecker(usr_replace_fiils_by_currentcolor)

        usr_make_one_line: str = input("[>] Do you want to make all SVG's in one line? [y/n]: ").lower()
        self._yornchecker(usr_make_one_line)

        return [usr_path, usr_replace_fiils_by_currentcolor, usr_make_one_line]

    def scriptinit(self):
        settings = self._usrinput()
        match settings[1]:
            case "y":
                self._replace_fills_by_currentcolor(settings[0])
                self._remove_xml_tag_and_generator_info(settings[0])
        match settings[2]:
            case "y":
                self._make_one_line(settings[0])


if __name__ == "__main__":
    script = Script()
    script.scriptinit()
        
