'''
LICENSED under Apache 2.0 (http://directory.fsf.org/wiki/License:Apache2.0)
Created by: Md Shahedul Alam (Research Assistant, Aalto University)
            Mohammad Azangoo (Project Researcher, Aalto University)
			Udayanto Dwi Atmojo
February, 2020
'''
from tkinter import *
import time
import json


# ----------------------------------------------------------------------------------------------------------------------------------------------#
COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white',
          'old lace',
          'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque',
          'peach puff',
          'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue',
          'lavender',
          'lavender blush', 'misty rose', 'dark slate gray', 'dim gray',
          'slate gray',
          'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy',
          'cornflower blue', 'dark slate blue',
          'slate blue', 'medium slate blue', 'light slate blue', 'medium blue',
          'royal blue', 'blue',
          'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue',
          'steel blue', 'light steel blue',
          'light blue', 'powder blue', 'pale turquoise', 'dark turquoise',
          'medium turquoise', 'turquoise',
          'cyan', 'light cyan', 'cadet blue', 'medium aquamarine',
          'aquamarine', 'dark green', 'dark olive green',
          'dark sea green', 'sea green', 'medium sea green', 'light sea green',
          'pale green', 'spring green',
          'lawn green', 'medium spring green', 'green yellow', 'lime green',
          'yellow green',
          'forest green', 'olive drab', 'dark khaki', 'khaki',
          'pale goldenrod', 'light goldenrod yellow',
          'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod',
          'dark goldenrod', 'rosy brown',
          'indian red', 'saddle brown', 'sandy brown',
          'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
          'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink',
          'deep pink', 'pink', 'light pink',
          'pale violet red', 'maroon', 'medium violet red', 'violet red',
          'medium orchid', 'dark orchid', 'dark violet', 'blue violet',
          'purple', 'medium purple',
          'thistle', 'snow2', 'snow3',
          'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1',
          'AntiqueWhite2',
          'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4',
          'PeachPuff2',
          'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3',
          'NavajoWhite4',
          'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2',
          'cornsilk3',
          'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3',
          'honeydew4',
          'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2',
          'MistyRose3',
          'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1',
          'SlateBlue2', 'SlateBlue3',
          'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4',
          'blue2', 'blue4',
          'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1',
          'SteelBlue2',
          'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3',
          'DeepSkyBlue4',
          'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1',
          'LightSkyBlue2',
          'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2',
          'SlateGray3',
          'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2',
          'LightSteelBlue3',
          'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3',
          'LightBlue4',
          'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1',
          'PaleTurquoise2',
          'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2',
          'CadetBlue3',
          'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4',
          'cyan2', 'cyan3',
          'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3',
          'DarkSlateGray4',
          'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2',
          'DarkSeaGreen3',
          'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1',
          'PaleGreen2',
          'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3',
          'SpringGreen4',
          'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3',
          'chartreuse4',
          'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1',
          'DarkOliveGreen2',
          'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3',
          'khaki4',
          'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3',
          'LightGoldenrod4',
          'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3',
          'yellow4',
          'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3',
          'goldenrod4',
          'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3',
          'DarkGoldenrod4',
          'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1',
          'IndianRed2',
          'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3',
          'sienna4', 'burlywood1',
          'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2',
          'wheat3', 'wheat4', 'tan1',
          'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3',
          'firebrick1', 'firebrick2',
          'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4',
          'salmon1', 'salmon2',
          'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4',
          'orange2',
          'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3',
          'DarkOrange4',
          'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3',
          'tomato4', 'OrangeRed2',
          'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2',
          'DeepPink3', 'DeepPink4',
          'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2',
          'pink3', 'pink4',
          'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4',
          'PaleVioletRed1',
          'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1',
          'maroon2',
          'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3',
          'VioletRed4',
          'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3',
          'orchid4', 'plum1',
          'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2',
          'MediumOrchid3',
          'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3',
          'DarkOrchid4',
          'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1',
          'MediumPurple2',
          'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3',
          'thistle4',
          'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7',
          'gray8', 'gray9', 'gray10',
          'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17',
          'gray18', 'gray19',
          'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26',
          'gray27', 'gray28',
          'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35',
          'gray36', 'gray37',
          'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45',
          'gray46', 'gray47',
          'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54',
          'gray55', 'gray56',
          'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63',
          'gray64', 'gray65',
          'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72',
          'gray73', 'gray74',
          'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81',
          'gray82', 'gray83',
          'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90',
          'gray91', 'gray92',
          'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']


class RFID_graphic:
    def __init__(self, number, width, height):
        self.number = number  # number of RFID readers
        self.width = width  # width of canvas
        self.height = height  # height of canvas

        # Initial part:
        root = Tk()
        root.title("Factory of the Future Test Platform")
        self.factory = Canvas(root, width=self.width, height=self.height,
                              bg='black')  # General canvas
        self.factory.pack(fill=BOTH)

        text = self.factory.create_text(self.width / 2, 30, text="���<< Aalto University >>���", fill="yellow", font=("Helvectica", "35"))
        text = self.factory.create_text(self.width / 2, 70, text="Factory of the Future, EnAS Demonstrator Plant", fill="white", font=("Helvectica", "25"))
        text = self.factory.create_text(self.width / 2, 110, text="OPC UA Based Monitoring System (under construction...)", fill="gray", font=("Helvectica", "25"))

        square = self.factory.create_rectangle(200, 200, self.width - 200, 250, fill="red")  # conveyor
        square = self.factory.create_rectangle(200, 200, 250, self.height - 200, fill="red")
        square = self.factory.create_rectangle(200, self.height - 250, self.width - 200, self.height - 200, fill="red")
        square = self.factory.create_rectangle(self.width - 300, 200, self.width - 250, self.height - 200, fill="red")

        square = self.factory.create_rectangle(350, 170, 400, 200, fill="white")
        text = self.factory.create_text(375, 185, text="ST3", fill="black", font=("Helvectica", "10"))

        square = self.factory.create_rectangle(150, 500, 200, 530, fill="white")
        text = self.factory.create_text(175, 515, text="ST2", fill="black", font=("Helvectica", "10"))

        square = self.factory.create_rectangle(650, 170, 700, 200, fill="white")
        text = self.factory.create_text(675, 185, text="ST4", fill="black", font=("Helvectica", "10"))

        square = self.factory.create_rectangle(self.width - 350, self.height - 200, self.width - 400, self.height - 170, fill="white")
        text = self.factory.create_text(self.width - 375, self.height - 185, text="ST1", fill="black", font=("Helvectica", "10"))

        square = self.factory.create_rectangle(self.width - 250, 500, self.width - 200, 530, fill="white")
        text = self.factory.create_text(self.width - 225, 515, text="ST5", fill="black", font=("Helvectica", "10"))

        self.Tag_circle = [0 for x in range(self.number + 1)]  # Tags Initialisation
        self.Tag_text = [0 for x in range(self.number + 1)]  # Tags Initialisation

        self.run = 0  # Running-Blinking Initialisation
        self.running_text1 = self.factory.create_text((self.width / 2), (self.height / 2), text="Start Up ....", fill="gold2", font=("Helvectica", "30", "bold"))
        self.running_text2 = self.factory.create_text((self.width / 2), (self.height / 2), text="Start Up ....", fill="gold2", font=("Helvectica", "30", "bold"))

    def clearance(self):  # for initial clearance
        for i in range(self.number + 1):
            self.factory.delete(self.Tag_circle[i - 1])
            self.factory.delete(self.Tag_text[i - 1])

    def implement(self, RFID_NO, value):  # Tag function
        if (RFID_NO) == 1:
            self.factory.delete(self.Tag_circle[value])
            self.factory.delete(self.Tag_text[value])
            self.Tag_circle[value] = self.factory.create_oval(self.width - 355, self.height - 245, self.width - 395, self.height - 205, fill=COLORS[61])
            self.Tag_text[value] = self.factory.create_text(self.width - 375, self.height - 225, text=str(value), fill="blue", font=("Helvectica", "10"))

        elif (RFID_NO) == 2:
            self.factory.delete(self.Tag_circle[value])
            self.factory.delete(self.Tag_text[value])
            self.Tag_circle[value] = self.factory.create_oval(205, 495, 245, 535, fill=COLORS[61])
            self.Tag_text[value] = self.factory.create_text(225, 515, text=str(value), fill="blue", font=("Helvectica", "10"))

        elif (RFID_NO) == 3:
            self.factory.delete(self.Tag_circle[value])
            self.factory.delete(self.Tag_text[value])
            self.Tag_circle[value] = self.factory.create_oval(355, 205, 395, 245, fill=COLORS[61])
            self.Tag_text[value] = self.factory.create_text(375, 225, text=str(value), fill="blue", font=("Helvectica", "10"))

        elif (RFID_NO) == 4:
            self.factory.delete(self.Tag_circle[value])
            self.factory.delete(self.Tag_text[value])
            self.Tag_circle[value] = self.factory.create_oval(655, 205, 695, 245, fill=COLORS[61])
            self.Tag_text[value] = self.factory.create_text(675, 225, text=str(value), fill="blue", font=("Helvectica", "10"))

        elif (RFID_NO) == 5:
            self.factory.delete(self.Tag_circle[int(10)])
            self.factory.delete(self.Tag_text[int(10)])
            self.factory.delete(self.Tag_circle[value])
            self.factory.delete(self.Tag_text[value])
            self.Tag_circle[value] = self.factory.create_oval(self.width - 295, 495, self.width - 255, 535, fill=COLORS[61])
            self.Tag_text[value] = self.factory.create_text(self.width - 275, 515, text=str(value), fill="blue", font=("Helvectica", "10"))

    def running_one(self, enas_data):  # Running Conveyor One Blinking
        self.run += 1
        self.factory.delete(self.running_text1)
        self.factory.delete(self.running_text2)

        square = self.factory.create_rectangle(350, 170, 400, 200, fill="white")
        text = self.factory.create_text(375, 185, text="ST3", fill="black", font=("Helvectica", "10"))

        square = self.factory.create_rectangle(150, 500, 200, 530, fill="white")
        text = self.factory.create_text(175, 515, text="ST2", fill="black", font=("Helvectica", "10"))

        square = self.factory.create_rectangle(650, 170, 700, 200, fill="white")
        text = self.factory.create_text(675, 185, text="ST4", fill="black", font=("Helvectica", "10"))

        square = self.factory.create_rectangle(self.width - 350, self.height - 200, self.width - 400, self.height - 170, fill="spring green")
        text = self.factory.create_text(self.width - 375, self.height - 185, text="ST1", fill="black", font=("Helvectica", "10"))

        square = self.factory.create_rectangle(self.width - 250, 500, self.width - 200, 530, fill="white")
        text = self.factory.create_text(self.width - 225, 515, text="ST5", fill="black", font=("Helvectica", "10"))

        #if enas_data["CNV_One_RFID_1"]:
            #graph.implement(1, 20)
        if (self.run % 5) == 0:
            if enas_data["CNV_One_Direction"] == "Left":
                self.running_text1 = self.factory.create_text(400, self.height - 225, text="                     ⮘⮘", fill="gold2", font=("Helvectica", "30", "bold"))
            elif enas_data["CNV_One_Direction"] == "Right":
                self.running_text1 = self.factory.create_text(400, self.height - 225, text="⮚⮚                     ", fill="gold2", font=("Helvectica", "30", "bold"))
        elif (self.run % 5) == 1:
            if enas_data["CNV_One_Direction"] == "Left":
                self.running_text1 = self.factory.create_text(400, self.height - 225, text="               ⮘⮘      ", fill="gold2", font=("Helvectica", "30", "bold"))
            elif enas_data["CNV_One_Direction"] == "Right":
                self.running_text1 = self.factory.create_text(400, self.height - 225, text="      ⮚⮚                ", fill="gold2", font=("Helvectica", "30", "bold"))
        elif (self.run % 5) == 2:
            if enas_data["CNV_One_Direction"] == "Left":
                self.running_text1 = self.factory.create_text(400, self.height - 225, text="           ⮘⮘           ", fill="gold2", font=("Helvectica", "30", "bold"))
            elif enas_data["CNV_One_Direction"] == "Right":
                self.running_text1 = self.factory.create_text(400, self.height - 225, text="           ⮚⮚           ", fill="gold2", font=( "Helvectica", "30", "bold"))
        elif (self.run % 5) == 3:
            if enas_data["CNV_One_Direction"] == "Left":
                self.running_text1 = self.factory.create_text(400, self.height - 225, text="      ⮘⮘                ", fill="gold2", font=("Helvectica", "30", "bold"))
            elif enas_data["CNV_One_Direction"] == "Right":
                self.running_text1 = self.factory.create_text(400, self.height - 225, text="                ⮚⮚      ", fill="gold2", font=("Helvectica", "30", "bold"))
        else:
            if enas_data["CNV_One_Direction"] == "Left":
                self.running_text1 = self.factory.create_text(400, self.height - 225, text="⮘⮘                      ", fill="gold2", font=("Helvectica", "30", "bold"))
            elif enas_data["CNV_One_Direction"] == "Right":
                self.running_text1 = self.factory.create_text(400, self.height - 225, text="                      ⮚⮚", fill="gold2", font=("Helvectica", "30", "bold"))

    def running_two(self, enas_data):  # Running Conveyor Two Blinking
        self.run += 1
        self.factory.delete(self.running_text1)
        self.factory.delete(self.running_text2)

        square = self.factory.create_rectangle(350, 170, 400, 200, fill="white")
        text = self.factory.create_text(375, 185, text="ST3", fill="black", font=("Helvectica", "10"))

        square = self.factory.create_rectangle(150, 500, 200, 530, fill="spring green")
        text = self.factory.create_text(175, 515, text="ST2", fill="black", font=("Helvectica", "10"))

        square = self.factory.create_rectangle(650, 170, 700, 200, fill="white")
        text = self.factory.create_text(675, 185, text="ST4", fill="black", font=("Helvectica", "10"))

        square = self.factory.create_rectangle(self.width - 350, self.height - 200, self.width - 400, self.height - 170, fill="white")
        text = self.factory.create_text(self.width - 375, self.height - 185, text="ST1", fill="black", font=("Helvectica", "10"))

        square = self.factory.create_rectangle(self.width - 250, 500, self.width - 200, 530, fill="white")
        text = self.factory.create_text(self.width - 225, 515, text="ST5", fill="black", font=("Helvectica", "10"))

        #if enas_data["CNV_Two_RFID_2"]:
            #graph.implement(2, 20)
        if (self.run % 5) == 0:
            if enas_data["CNV_Two_Direction"] == "Up":
                self.running_text1 = self.factory.create_text(225, self.height - 275, text="⮙", fill="gold2", font=("Helvectica", "30", "bold"))
                self.running_text2 = self.factory.create_text(225, self.height - 305, text="⮙", fill="gold2", font=("Helvectica", "30", "bold"))
            elif enas_data["CNV_Two_Direction"] == "Down":
                self.running_text1 = self.factory.create_text(225, self.height - 675, text="⮛", fill="gold2", font=("Helvectica", "30", "bold"))
                self.running_text2 = self.factory.create_text(225, self.height - 705, text="⮛", fill="gold2", font=("Helvectica", "30", "bold"))

        elif (self.run % 5) == 1:
            if enas_data["CNV_Two_Direction"] == "Up":
                self.running_text1 = self.factory.create_text(225, self.height - 375, text="⮙", fill="gold2", font=("Helvectica", "30", "bold"))
                self.running_text2 = self.factory.create_text(225, self.height - 405, text="⮙", fill="gold2", font=("Helvectica", "30", "bold"))
            elif enas_data["CNV_Two_Direction"] == "Down":
                self.running_text1 = self.factory.create_text(225, self.height - 575, text="⮛", fill="gold2", font=("Helvectica", "30", "bold"))
                self.running_text2 = self.factory.create_text(225, self.height - 605, text="⮛", fill="gold2", font=("Helvectica", "30", "bold"))

        elif (self.run % 5) == 2:
            if enas_data["CNV_Two_Direction"] == "Up":
                self.running_text1 = self.factory.create_text(225, self.height - 475, text="⮙", fill="gold2", font=("Helvectica", "30", "bold"))
                self.running_text2 = self.factory.create_text(225, self.height - 505, text="⮙", fill="gold2", font=("Helvectica", "30", "bold"))
            elif enas_data["CNV_Two_Direction"] == "Down":
                self.running_text1 = self.factory.create_text(225, self.height - 475, text="⮛", fill="gold2", font=("Helvectica", "30", "bold"))
                self.running_text2 = self.factory.create_text(225, self.height - 505, text="⮛", fill="gold2", font=("Helvectica", "30", "bold"))

        elif (self.run % 5) == 3:
            if enas_data["CNV_Two_Direction"] == "Up":
                self.running_text1 = self.factory.create_text(225, self.height - 575, text="⮙", fill="gold2", font=("Helvectica", "30", "bold"))
                self.running_text2 = self.factory.create_text(225, self.height - 605, text="⮙", fill="gold2", font=("Helvectica", "30", "bold"))
            elif enas_data["CNV_Two_Direction"] == "Down":
                self.running_text1 = self.factory.create_text(225, self.height - 375, text="⮛", fill="gold2", font=("Helvectica", "30", "bold"))
                self.running_text2 = self.factory.create_text(225, self.height - 405, text="⮛", fill="gold2", font=("Helvectica", "30", "bold"))
        else:
            if enas_data["CNV_Two_Direction"] == "Up":
                self.running_text1 = self.factory.create_text(225, self.height - 675, text="⮙", fill="gold2", font=("Helvectica", "30", "bold"))
                self.running_text2 = self.factory.create_text(225, self.height - 705, text="⮙", fill="gold2", font=("Helvectica", "30", "bold"))
            elif enas_data["CNV_Two_Direction"] == "Down":
                self.running_text1 = self.factory.create_text(225, self.height - 275, text="⮛", fill="gold2", font=("Helvectica", "30", "bold"))
                self.running_text2 = self.factory.create_text(225, self.height - 305, text="⮛", fill="gold2", font=("Helvectica", "30", "bold"))

    def running_three(self, enas_data):  # Running Conveyor Three Blinking
        self.run += 1
        self.factory.delete(self.running_text1)
        self.factory.delete(self.running_text2)

        square = self.factory.create_rectangle(350, 170, 400, 200, fill="spring green")
        text = self.factory.create_text(375, 185, text="ST3", fill="black", font=("Helvectica", "10"))

        square = self.factory.create_rectangle(150, 500, 200, 530, fill="white")
        text = self.factory.create_text(175, 515, text="ST2", fill="black", font=("Helvectica", "10"))

        square = self.factory.create_rectangle(650, 170, 700, 200, fill="spring green")
        text = self.factory.create_text(675, 185, text="ST4", fill="black", font=("Helvectica", "10"))

        square = self.factory.create_rectangle(self.width - 350, self.height - 200, self.width - 400, self.height - 170, fill="white")
        text = self.factory.create_text(self.width - 375, self.height - 185, text="ST1", fill="black", font=("Helvectica", "10"))

        square = self.factory.create_rectangle(self.width - 250, 500, self.width - 200, 530, fill="white")
        text = self.factory.create_text(self.width - 225, 515, text="ST5", fill="black", font=("Helvectica", "10"))
        '''
        if enas_data["CNV_Three_RFID_3"]:
            graph.implement(3, 10)
        if enas_data["CNV_Three_RFID_4"]:
            graph.implement(4, 20)
'''
        if (self.run % 5) == 0:
            if enas_data["CNV_Three_Direction"] == "Right":
                self.running_text2 = self.factory.create_text(self.width - 400, 225, text="⮚⮚                     ", fill="gold2", font=("Helvectica", "30", "bold"))
            elif enas_data["CNV_Three_Direction"] == "Left":
                self.running_text2 = self.factory.create_text(self.width - 400, 225, text="                     ⮘⮘", fill="gold2", font=("Helvectica", "30", "bold"))
        elif (self.run % 5) == 1:
            if enas_data["CNV_Three_Direction"] == "Right":
                self.running_text2 = self.factory.create_text(self.width - 400, 225, text="      ⮚⮚                ", fill="gold2", font=("Helvectica", "30", "bold"))
            elif enas_data["CNV_Three_Direction"] == "Left":
                self.running_text2 = self.factory.create_text(self.width - 400, 225, text="               ⮘⮘      ", fill="gold2", font=("Helvectica", "30", "bold"))
        elif (self.run % 5) == 2:
            if enas_data["CNV_Three_Direction"] == "Right":
                self.running_text2 = self.factory.create_text(self.width - 400, 225, text="           ⮚⮚           ", fill="gold2", font=( "Helvectica", "30", "bold"))
            elif enas_data["CNV_Three_Direction"] == "Left":
                self.running_text2 = self.factory.create_text(self.width - 400, 225, text="           ⮘⮘           ", fill="gold2", font=("Helvectica", "30", "bold"))
        elif (self.run % 5) == 3:
            if enas_data["CNV_Three_Direction"] == "Right":
                self.running_text2 = self.factory.create_text(self.width - 400, 225, text="                ⮚⮚      ", fill="gold2", font=("Helvectica", "30", "bold"))
            elif enas_data["CNV_Three_Direction"] == "Left":
                self.running_text2 = self.factory.create_text(self.width - 400, 225, text="      ⮘⮘                ", fill="gold2", font=("Helvectica", "30", "bold"))
        else:
            if enas_data["CNV_Three_Direction"] == "Right":
                self.running_text2 = self.factory.create_text(self.width - 400, 225, text="                      ⮚⮚", fill="gold2", font=("Helvectica", "30", "bold"))
            elif enas_data["CNV_Three_Direction"] == "Left":
                self.running_text2 = self.factory.create_text(self.width - 400, 225, text="⮘⮘                      ", fill="gold2", font=("Helvectica", "30", "bold"))

    def running_four(self, enas_data):  # Running Conveyor Four Blinking
        self.run += 1
        self.factory.delete(self.running_text1)
        self.factory.delete(self.running_text2)

        square = self.factory.create_rectangle(350, 170, 400, 200, fill="white")
        text = self.factory.create_text(375, 185, text="ST3", fill="black", font=("Helvectica", "10"))

        square = self.factory.create_rectangle(150, 500, 200, 530, fill="white")
        text = self.factory.create_text(175, 515, text="ST2", fill="black", font=("Helvectica", "10"))

        square = self.factory.create_rectangle(650, 170, 700, 200, fill="white")
        text = self.factory.create_text(675, 185, text="ST4", fill="black", font=("Helvectica", "10"))

        square = self.factory.create_rectangle(self.width - 350, self.height - 200, self.width - 400, self.height - 170, fill="white")
        text = self.factory.create_text(self.width - 375, self.height - 185, text="ST1", fill="black", font=("Helvectica", "10"))

        square = self.factory.create_rectangle(self.width - 250, 500, self.width - 200, 530, fill="spring green")
        text = self.factory.create_text(self.width - 225, 515, text="ST5", fill="black", font=("Helvectica", "10"))

        #if enas_data["CNV_Four_RFID_5"]:
            #graph.implement(5, 20)
        if (self.run % 5) == 0:
            if enas_data["CNV_Four_Direction"] == "Down":
                self.running_text1 = self.factory.create_text(1025, self.height - 675, text="⮛", fill="gold2", font=("Helvectica", "30", "bold"))
                self.running_text2 = self.factory.create_text(1025, self.height - 705, text="⮛", fill="gold2", font=("Helvectica", "30", "bold"))
            elif enas_data["CNV_Four_Direction"] == "Up":
                self.running_text1 = self.factory.create_text(1025, self.height - 275, text="⮙", fill="gold2", font=("Helvectica", "30", "bold"))
                self.running_text2 = self.factory.create_text(1025, self.height - 305, text="⮙", fill="gold2", font=("Helvectica", "30", "bold"))
        elif (self.run % 5) == 1:
            if enas_data["CNV_Four_Direction"] == "Down":
                self.running_text1 = self.factory.create_text(1025, self.height - 575, text="⮛", fill="gold2", font=("Helvectica", "30", "bold"))
                self.running_text2 = self.factory.create_text(1025, self.height - 605, text="⮛", fill="gold2", font=("Helvectica", "30", "bold"))
            elif enas_data["CNV_Four_Direction"] == "Up":
                self.running_text1 = self.factory.create_text(1025, self.height - 375, text="⮙", fill="gold2", font=("Helvectica", "30", "bold"))
                self.running_text2 = self.factory.create_text(1025, self.height - 405, text="⮙", fill="gold2", font=("Helvectica", "30", "bold"))
        elif (self.run % 5) == 2:
            if enas_data["CNV_Four_Direction"] == "Down":
                self.running_text1 = self.factory.create_text(1025, self.height - 475, text="⮛", fill="gold2", font=("Helvectica", "30", "bold"))
                self.running_text2 = self.factory.create_text(1025, self.height - 505, text="⮛", fill="gold2", font=("Helvectica", "30", "bold"))
            elif enas_data["CNV_Four_Direction"] == "Up":
                self.running_text1 = self.factory.create_text(1025, self.height - 475, text="⮙", fill="gold2", font=("Helvectica", "30", "bold"))
                self.running_text2 = self.factory.create_text(1025, self.height - 505, text="⮙", fill="gold2", font=("Helvectica", "30", "bold"))
        elif (self.run % 5) == 3:
            if enas_data["CNV_Four_Direction"] == "Down":
                self.running_text1 = self.factory.create_text(1025, self.height - 375, text="⮛", fill="gold2", font=("Helvectica", "30", "bold"))
                self.running_text2 = self.factory.create_text(1025, self.height - 405, text="⮛", fill="gold2", font=("Helvectica", "30", "bold"))
            elif enas_data["CNV_Four_Direction"] == "Up":
                self.running_text1 = self.factory.create_text(1025, self.height - 575, text="⮙", fill="gold2", font=("Helvectica", "30", "bold"))
                self.running_text2 = self.factory.create_text(1025, self.height - 605, text="⮙", fill="gold2", font=("Helvectica", "30", "bold"))
        else:
            if enas_data["CNV_Four_Direction"] == "Down":
                self.running_text1 = self.factory.create_text(1025, self.height - 275, text="⮛", fill="gold2", font=("Helvectica", "30", "bold"))
                self.running_text2 = self.factory.create_text(1025, self.height - 305, text="⮛", fill="gold2", font=("Helvectica", "30", "bold"))
            elif enas_data["CNV_Four_Direction"] == "Up":
                self.running_text1 = self.factory.create_text(1025, self.height - 675, text="⮙", fill="gold2", font=("Helvectica", "30", "bold"))
                self.running_text2 = self.factory.create_text(1025, self.height - 705, text="⮙", fill="gold2", font=("Helvectica", "30", "bold"))


graph = RFID_graphic(20, 1300, 1000)
graph.factory.update()

while True:
    with open("enas_data.json") as api_file:
        enas_data = json.load(api_file)
    for i in range(5):  # 1 sec delay
        time.sleep(0.2)
        if enas_data["CNV_One_State"]:
            graph.running_one(enas_data)
            graph.factory.update()
        elif enas_data["CNV_Two_State"]:
            graph.running_two(enas_data)
            graph.factory.update()
        elif enas_data["CNV_Three_State"]:
            graph.running_three(enas_data)
            graph.factory.update()
        elif enas_data["CNV_Four_State"]:
            graph.running_four(enas_data)
            graph.factory.update()
        else:
            pass
