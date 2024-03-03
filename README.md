# Adobe Illustrator SVG Beautifier

This is a simple script that allows you to quickly edit your created SVG icons in Adobe Illustrator to conveniently insert them into your website.

You will be able to remove all HEX colors by replacing them with `currentColor;` or make your SVG icon code a single line. Well, or, do it all together!

Here is example SVG icon you made in Adobe Illustrator:
```xml
<?xml version="1.0" encoding="utf-8"?>
<!-- Generator: Adobe Illustrator 27.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->
<svg version="1.1" id="icon" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 32 32" style="enable-background:new 0 0 32 32;" xml:space="preserve">
<style type="text/css">
	.st0{fill:#006837;}
</style>
<path class="st0" d="M30,4v8c0,1.1-0.9,2-2,2c-0.5,0-1-0.2-1.4-0.6C26.2,13,26,12.5,26,12V8.8l-9.8,9.8c-0.8,0.8-2,0.8-2.8,0
	c-0.4-0.4-0.6-0.9-0.6-1.4c0-0.5,0.2-1,0.6-1.4L23.2,6H20c-1.1,0-2-0.9-2-2c0-1.1,0.9-2,2-2h8C29.1,2,30,2.9,30,4z"/>
<path class="st0" d="M32,20v4c0,4.4-3.6,8-8,8H8c-4.4,0-8-3.6-8-8V8c0-4.4,3.6-8,8-8h4c1.1,0,2,0.9,2,2c0,0.5-0.2,1-0.6,1.4
	C13,3.8,12.5,4,12,4H8C5.8,4,4,5.8,4,8v16c0,2.2,1.8,4,4,4h16c2.2,0,4-1.8,4-4v-4c0-0.5,0.2-1,0.6-1.4C29,18.2,29.5,18,30,18
	C31.1,18,32,18.9,32,20z"/>
</svg>
```
And here is how script modify icon:
```xml
<?xml version="1.0" ?><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="icon" x="0px" y="0px" viewBox="0 0 32 32" style="enable-background:new 0 0 32 32;" xml:space="preserve"> <style type="text/css">.st0{fill:currentColor;}</style> <path class="st0" d="M30,4v8c0,1.1-0.9,2-2,2c-0.5,0-1-0.2-1.4-0.6C26.2,13,26,12.5,26,12V8.8l-9.8,9.8c-0.8,0.8-2,0.8-2.8,0 c-0.4-0.4-0.6-0.9-0.6-1.4c0-0.5,0.2-1,0.6-1.4L23.2,6H20c-1.1,0-2-0.9-2-2c0-1.1,0.9-2,2-2h8C29.1,2,30,2.9,30,4z"/> <path class="st0" d="M32,20v4c0,4.4-3.6,8-8,8H8c-4.4,0-8-3.6-8-8V8c0-4.4,3.6-8,8-8h4c1.1,0,2,0.9,2,2c0,0.5-0.2,1-0.6,1.4 C13,3.8,12.5,4,12,4H8C5.8,4,4,5.8,4,8v16c0,2.2,1.8,4,4,4h16c2.2,0,4-1.8,4-4v-4c0-0.5,0.2-1,0.6-1.4C29,18.2,29.5,18,30,18 C31.1,18,32,18.9,32,20z"/></svg>
```
# Usage
- Draw the icons in Adobe Illustrator, place them in some directory
- Run the script
- Specify the path to the directory with icons in the console input
- Select what you want by pressing "Y" or "N" 
- Enjoy the formatted icons :)
# Requirements
- Python 3.10 or higher
