# -*- coding: utf-8 -*-
import sys
import os
from Screens.Screen import Screen
from Components.MenuList import MenuList
from Components.Sources.StaticText import StaticText
from Components.ActionMap import ActionMap
from Screens.Console import Console
from Screens.MessageBox import MessageBox
from Components.Label import Label
from Components.Pixmap import Pixmap
from Components.Sources.Clock import Clock
from Tools.Directories import fileExists, resolveFilename, SCOPE_PLUGINS
from Plugins.Plugin import PluginDescriptor
from enigma import ePoint, eTimer, quitMainloop
from Screens.Standby import TryQuitMainloop

PLUGIN_PATH = resolveFilename(SCOPE_PLUGINS, "Extensions/EmilPanelPro")
PLUGIN_VERSION = "1.0"
PLUGIN_DESC = "Emil Panel Pro - Enigma2 Tools"

from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Screens.Console import Console
from Screens.Standby import TryQuitMainloop
from Components.Label import Label
from Components.Pixmap import Pixmap
from Components.ActionMap import ActionMap
from Components.Sources.Clock import Clock
from enigma import getDesktop, ePoint
import os

PLUGIN_PATH = "/usr/lib/enigma2/python/Plugins/Extensions/FreePanelDMOS/images"

HD_SKIN = """
<screen position="center,center" size="1280,720" title="Emil Panel Pro">
    <ePixmap position="0,0" zPosition="0" size="1280,720" pixmap="%s/panel.png" transparent="1" alphatest="blend" />
    <eLabel position="0,0" zPosition="-10" size="1280,720" backgroundColor="black" />
    <widget name="frame" position="60,150" size="100,100" pixmap="%s/pic_frame2.png" zPosition="3" transparent="1" alphatest="blend" />
    %s
    <eLabel position="60,640" size="150,30" zPosition="3" backgroundColor="#C11B17" transparent="0" />
    <widget name="key_red" position="60,625" size="150,60" valign="center" halign="center" zPosition="4" foregroundColor="white" font="Regular;26" transparent="1" text="Exit" />
    <eLabel position="230,640" size="150,30" zPosition="3" backgroundColor="#347235" transparent="0" />
    <widget name="key_green" position="230,625" size="150,60" valign="center" halign="center" zPosition="4" foregroundColor="white" font="Regular;26" transparent="1" text="Ok" />
    <eLabel position="400,640" size="150,30" zPosition="3" backgroundColor="#EAC117" transparent="0" />
    <widget name="key_yellow" position="400,625" size="150,60" valign="center" halign="center" zPosition="4" foregroundColor="white" font="Regular;26" transparent="1" text="Update" />
    <eLabel position="570,640" size="150,30" zPosition="3" backgroundColor="#153E7E" transparent="0" />
    <widget name="key_blue" position="570,625" size="150,60" valign="center" halign="center" zPosition="4" foregroundColor="white" font="Regular;26" transparent="1" text="Restart" />
    <widget name="sort" position="820,626" zPosition="4" size="400,60" font="Regular; 28" foregroundColor="#0049bbff" backgroundColor="#40000000" transparent="1" halign="left" valign="center" />
    <eLabel name="sort_index" position="790,632" size="36,36" backgroundColor="#40000000" halign="center" valign="center" transparent="1" cornerRadius="18" font="Regular; 28" zPosition="1" text="0" foregroundColor="#0049bbff" />
    <widget source="session.VideoPicture" render="Pig" position="750,120" size="480,320" zPosition="1" backgroundColor="#ff000000" />
    <ePixmap position="850,460" zPosition="2" size="300,150" pixmap="%s/emilpanel.png" alphatest="on" />
    <widget source="global.CurrentTime" render="Label" position="1000,626" size="250,50" font="Regular;26" halign="left" valign="center" foregroundColor="#0049bbff" backgroundColor="#20000000" transparent="1" zPosition="2">
        <convert type="ClockToText">Default</convert>
    </widget>
</screen>
"""

FHD_SKIN = """
<screen position="center,center" size="1920,1080" title="Emil Panel Pro">
    <ePixmap position="0,0" zPosition="0" size="1920,1080" pixmap="%s/panel.png" transparent="1" alphatest="blend" />
    <eLabel position="0,0" zPosition="-10" size="1920,1080" backgroundColor="black" />
    <widget name="frame" position="100,210" size="150,150" pixmap="%s/pic_frame2.png" zPosition="3" transparent="1" alphatest="blend" />
    %s
    <eLabel position="100,1000" size="200,40" zPosition="3" backgroundColor="#C11B17" transparent="0" />
    <widget name="key_red" position="100,980" size="200,80" valign="center" halign="center" zPosition="4" foregroundColor="white" font="Regular;40" transparent="1" text="Exit" />
    <eLabel position="320,1000" size="200,40" zPosition="3" backgroundColor="#347235" transparent="0" />
    <widget name="key_green" position="320,980" size="200,80" valign="center" halign="center" zPosition="4" foregroundColor="white" font="Regular;40" transparent="1" text="Ok" />
    <eLabel position="540,1000" size="200,40" zPosition="3" backgroundColor="#EAC117" transparent="0" />
    <widget name="key_yellow" position="540,980" size="200,80" valign="center" halign="center" zPosition="4" foregroundColor="white" font="Regular;40" transparent="1" text="Update" />
    <eLabel position="760,1000" size="200,40" zPosition="3" backgroundColor="#153E7E" transparent="0" />
    <widget name="key_blue" position="760,980" size="200,80" valign="center" halign="center" zPosition="4" foregroundColor="white" font="Regular;40" transparent="1" text="Restart" />
    <widget name="sort" position="1224,986" zPosition="4" size="675,84" font="Regular; 42" foregroundColor="#0049bbff" backgroundColor="#40000000" transparent="1" halign="left" valign="center" />
    <eLabel name="sort_index" position="1179,1002" size="52,52" backgroundColor="#40000000" halign="center" valign="center" transparent="1" cornerRadius="26" font="Regular; 42" zPosition="1" text="0" foregroundColor="#0049bbff" />
    <widget source="session.VideoPicture" render="Pig" position="1100,180" size="750,550" zPosition="1" backgroundColor="#ff000000" />
    <ePixmap position="1250,750" zPosition="2" size="500,250" pixmap="%s/emilpanel.png" alphatest="on" />
    <widget source="global.CurrentTime" render="Label" position="1650,986" size="350,60" font="Regular;36" halign="left" valign="center" foregroundColor="#0049bbff" backgroundColor="#20000000" transparent="1" zPosition="2">
        <convert type="ClockToText">Default</convert>
    </widget>
</screen>
"""

def generate_pixmaps(resolution="FHD"):
    pixmap_template = []
    if resolution == "HD":
        x_positions = [60, 200, 340, 480, 620]
        y_positions = [150, 270, 390]
        size = (100, 100)
        label_size = (100, 30)
        font_size = 20
        y_label_offset = 110
    else:
        x_positions = [100, 310, 525, 735, 940]
        y_positions = [210, 420, 635, 835]
        size = (150, 150)
        label_size = (150, 50)
        font_size = 24
        y_label_offset = 160
    index = 1
    for y in y_positions:
        for x in x_positions:
            pixmap_template.append('<widget name="pixmap%s" position="%s,%s" size="%s,%s" zPosition="2" transparent="1" alphatest="blend" />' % (index, x, y, size[0], size[1]))
            pixmap_template.append('<widget name="name_label%s" position="%s,%s" size="%s,%s" font="Regular;%s" halign="center" valign="center" zPosition="2" transparent="1" foregroundColor="white" />' % (index, x, y+y_label_offset, label_size[0], label_size[1], font_size))
            index += 1
            if index > 20:
                break
        if index > 20:
            break
    return "\n    ".join(pixmap_template)

class EmilPanelProScreen(Screen):
    def __init__(self, session):
        Screen.__init__(self, session)
        self.session = session
        if getDesktop(0).size().width() == 1920:
            self.skin = FHD_SKIN % (PLUGIN_PATH, PLUGIN_PATH, generate_pixmaps("FHD"), PLUGIN_PATH)
        else:
            self.skin = HD_SKIN % (PLUGIN_PATH, PLUGIN_PATH, generate_pixmaps("HD"), PLUGIN_PATH)
        self.main_menu_items = [
            ("Panels", self.openPanels, "panels.png"),
            ("Plugins", self.openPlugins, "plugins.png"),
            ("Channels", self.openChannels, "channels.png"),
            ("Feeds", self.openFeeds, "feeds.png"),
            ("Tools", self.openTools, "tools.png"),
            ("System", self.openSystem, "system.png"),
            ("Media", self.openMedia, "media.png"),
            ("Multiboot", self.openMultiboot, "multiboot.png"),
            ("Softcams", self.openSoftcams, "emu.png"),
            ("Backup", self.openBackup, "backup.png"),
            ("Restore", self.openRestore, "backup.png"),
            ("Skins", self.openSkins, "skins.png"),
            ("Remove", self.openRemove, "remove.png")
        ]
        self.selected_index = 0
        self.menu_stack = []
        self.sort_index = 0
        self["frame"] = Pixmap()
        self["key_red"] = Label("Exit")
        self["key_green"] = Label("Ok")
        self["key_yellow"] = Label("Update")
        self["key_blue"] = Label("Restart")
        self["sort"] = Label("Sort: Name")
        self["sort_index"] = Label("0")
        for i in range(1, 21):
            self["pixmap" + str(i)] = Pixmap()
            self["name_label" + str(i)] = Label("")
        self["CurrentTime"] = Clock()
        self["actions"] = ActionMap(
            ["OkCancelActions", "ColorActions", "DirectionActions", "NumberActions"], 
            {
                "ok": self.okPressed,
                "cancel": self.cancelPressed,
                "red": self.cancelPressed,
                "green": self.okPressed,
                "yellow": self.updatePressed,
                "blue": self.restartDevice,
                "up": self.upPressed,
                "down": self.downPressed,
                "left": self.leftPressed,
                "right": self.rightPressed,
                "0": self.toggleSort
            }, -1)
        self.onLayoutFinish.append(self.updateDisplay)

    def updateDisplay(self):
        items = self.main_menu_items
        for i in range(min(20, len(items))):
            pixmap_path = os.path.join(PLUGIN_PATH, items[i][2])
            if os.path.exists(pixmap_path):
                self["pixmap" + str(i+1)].instance.setPixmapFromFile(pixmap_path)
            self["name_label" + str(i+1)].setText(items[i][0])
            self["pixmap" + str(i+1)].show()
            self["name_label" + str(i+1)].show()
        for i in range(len(items), 20):
            self["pixmap" + str(i+1)].hide()
            self["name_label" + str(i+1)].hide()
        self.moveFrame(self.selected_index)
        self["sort_index"].setText(str(self.sort_index))

    def moveFrame(self, index):
        if getDesktop(0).size().width() == 1920:
            x_positions = [100, 310, 525, 735, 940]
            y_positions = [210, 420, 635, 835]
        else:
            x_positions = [60, 200, 340, 480, 620]
            y_positions = [150, 270, 390]
        row = index // len(x_positions)
        col = index % len(x_positions)
        if row < len(y_positions) and col < len(x_positions):
            self["frame"].instance.move(ePoint(x_positions[col], y_positions[row]))
            self["frame"].show()
        else:
            self["frame"].hide()

    def okPressed(self):
        if self.selected_index < len(self.main_menu_items):
            try:
                self.main_menu_items[self.selected_index][1]()
            except Exception as e:
                self.session.open(MessageBox, "Error: %s" % str(e), MessageBox.TYPE_ERROR)

    def cancelPressed(self):
        if self.menu_stack:
            self.menu_stack.pop()
            self.selected_index = 0
            self.updateDisplay()
        else:
            self.close()

    def upPressed(self):
        if self.selected_index >= 5:
            self.selected_index -= 5
            self.moveFrame(self.selected_index)

    def downPressed(self):
        if self.selected_index + 5 < len(self.main_menu_items):
            self.selected_index += 5
            self.moveFrame(self.selected_index)

    def leftPressed(self):
        row = self.selected_index // 5
        col = self.selected_index % 5
        if col > 0:
            self.selected_index -= 1
        elif row > 0:
            target = (row - 1) * 5 + 4
            self.selected_index = min(target, len(self.main_menu_items) - 1)
        self.moveFrame(self.selected_index)

    def rightPressed(self):
        row = self.selected_index // 5
        col = self.selected_index % 5
        if (col < 4) and (self.selected_index + 1 < len(self.main_menu_items)):
            self.selected_index += 1
        else:
            next_row_start = (row + 1) * 5
            if next_row_start < len(self.main_menu_items):
                self.selected_index = next_row_start
        self.moveFrame(self.selected_index)

    def toggleSort(self):
        sort_methods = ["Name", "Date", "Size", "Type"]
        current_method = self["sort"].getText().replace("Sort: ", "")
        if current_method in sort_methods:
            next_index = (sort_methods.index(current_method) + 1) % len(sort_methods)
        else:
            next_index = 0
        method = sort_methods[next_index]
        self["sort"].setText("Sort: " + method)
        if method == "Name":
            self.main_menu_items.sort(key=lambda x: x[0].lower())
        elif method == "Date":
            self.main_menu_items.sort(key=lambda x: os.path.getmtime(os.path.join(PLUGIN_PATH, x[2])) if os.path.exists(os.path.join(PLUGIN_PATH, x[2])) else 0, reverse=True)
        elif method == "Size":
            self.main_menu_items.sort(key=lambda x: os.path.getsize(os.path.join(PLUGIN_PATH, x[2])) if os.path.exists(os.path.join(PLUGIN_PATH, x[2])) else 0, reverse=True)
        elif method == "Type":
            self.main_menu_items.sort(key=lambda x: os.path.splitext(x[2])[1])
        self.selected_index = 0
        self.updateDisplay()

    def updatePressed(self):
        cmd = "wget https://gitlab.com/hanfy1971/plugin/-/raw/main/FreePanelDMOS/FreePanelDMOS.sh -O - | /bin/sh"
        self.session.open(Console, title="Updating...", cmdlist=[cmd])

    def restartDevice(self):
        self.session.open(TryQuitMainloop, 3)

    def openPanels(self):
        self.session.open(PanelsPanel)

    def openPlugins(self):
        self.session.open(PluginsPanel)

    def openChannels(self):
        self.session.open(ChannelsPanel)

    def openFeeds(self):
        self.session.open(FeedsPanel)

    def openTools(self):
        self.session.open(ToolsPanel)

    def openSystem(self):
        self.session.open(SystemPluginsPanel)

    def openMedia(self):
        self.session.open(MediaPanel)

    def openMultiboot(self):
        self.session.open(MultibootPanel)

    def openSoftcams(self):
        self.session.open(SoftcamsPanel)

    def openBackup(self):
        self.session.open(BackupPanel)

    def openRestore(self):
        self.session.open(RestorePanel)

    def openSkins(self):
        self.session.open(SkinsPanel)

    def openRemove(self):
        self.session.open(RemovePanel)


class BasePanel(Screen):
    def __init__(self, session, title, items):
        Screen.__init__(self, session)
        self.session = session
        self.title = title
        self.skin = """
        <screen position="center,center" size="600,500" title="%s">
            <widget name="menu" position="10,10" size="580,450" scrollbarMode="showOnDemand" />
            <ePixmap position="10,460" size="150,40" pixmap="skin_default/buttons/red.png" alphatest="blend" />
            <widget name="key_red" position="10,460" size="150,40" font="Regular;20" halign="center" valign="center" transparent="1" />
        </screen>""" % title
        self["menu"] = MenuList(items)
        self["key_red"] = Label("Exit")
        self["actions"] = ActionMap(["OkCancelActions", "ColorActions"], {
            "ok": self.okPressed,
            "cancel": self.close,
            "red": self.close
        }, -1)

    def okPressed(self):
        selection = self["menu"].getCurrent()
        self.session.open(MessageBox, "Selected: %s" % selection, MessageBox.TYPE_INFO)

class PanelsPanel(Screen):
    def __init__(self, session):
        Screen.__init__(self, session)
        self.skin = """
        <screen position="100,center" size="800,900" title="Panels Manager">
            <ePixmap position="0,0" size="800,900" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EmilPanelPro/images/back.png" zPosition="-1" />
            <widget source="title" render="Label" 
                position="50,30" size="700,60"
                font="Regular;50" halign="center" valign="center" 
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget name="list" position="50,110" size="700,680" 
                itemHeight="68" scrollbarMode="showOnDemand"
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget source="key_red" render="Label" position="50,820" size="200,50"
                backgroundColor="#9f1313" 
                halign="center" valign="center" font="Regular;32" 
                foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_green" render="Label" position="300,820" size="200,50"
                backgroundColor="#1f771f" 
                halign="center" valign="center" font="Regular;32" 
                foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_blue" render="Label" position="550,820" size="200,50"
                backgroundColor="#18188b" 
                halign="center" valign="center" font="Regular;32" 
                foregroundColor="#ffffff" zPosition="1"/>
        </screen>"""

        self["title"] = StaticText("Panels Manager")
        self["list"] = MenuList([])
        self["key_red"] = StaticText("Back")
        self["key_green"] = StaticText("Install")
        self["key_blue"] = StaticText("Restart")
        
        self["actions"] = ActionMap(["ColorActions", "OkCancelActions"], {
            "ok": self.confirmInstall,
            "cancel": self.close,
            "red": self.close,
            "green": self.confirmInstall,
            "blue": self.restartGUI
        }, -1)
        
        self.panels = [
            ("Ajpanel", "wget http://dreambox4u.com/emilnabil237/plugins/ajpanel/installer1.sh -O - | /bin/sh"),
            ("AjPanel Custom Menu All Panels", "wget https://dreambox4u.com/emilnabil237/plugins/ajpanel/emil-panel-all.sh -O - | /bin/sh"),
            ("Panel Lite By Emil Nabil", "wget https://dreambox4u.com/emilnabil237/plugins/ajpanel/new/emil-panel-lite.sh -O - | /bin/sh"),
            ("dreamosat-downloader", "wget https://dreambox4u.com/emilnabil237/plugins/dreamosat-downloader/installer.sh -O - | /bin/sh"),
            ("EmilPanelpro", "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/EmilPanelPro/emilpanelpro.sh -O - | /bin/sh"),           
            ("Epanel", "wget https://dreambox4u.com/emilnabil237/plugins/epanel/installer.sh -O - | /bin/sh"),
            ("linuxsat-panel", "wget https://raw.githubusercontent.com/Belfagor2005/LinuxsatPanel/main/installer.sh -O - | /bin/sh"),
            ("Levi45Emulator", "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/levi45emulator/installer.sh -O - | /bin/sh"),
            ("levi45-AddonsManager", "wget https://dreambox4u.com/emilnabil237/plugins/levi45-addonsmanager/installer.sh -O - | /bin/sh"),
            ("Levi45MulticamManager", "wget https://dreambox4u.com/emilnabil237/plugins/levi45multicammanager/installer.sh -O - | /bin/sh"),
            ("SatVenusPanel", "wget https://dreambox4u.com/emilnabil237/plugins/satvenuspanel/installer.sh -O - | /bin/sh"),
            ("Tspanel", "wget https://dreambox4u.com/emilnabil237/plugins/tspanel/installer.sh -O - | /bin/sh"),
            ("TvAddon-Panel", "wget https://dreambox4u.com/emilnabil237/plugins/tvaddon/installer.sh -O - | /bin/sh")
        ]
        
        self["list"].setList([name for name, cmd in self.panels])  
    
    def confirmInstall(self):
        idx = self["list"].getSelectedIndex()
        if idx < len(self.panels):
            panel_name = self.panels[idx][0]
            self.session.openWithCallback(
                self.installConfirmed,
                MessageBox,
                "Do you want to install %s ?" % panel_name,
                MessageBox.TYPE_YESNO
            )

    def installConfirmed(self, answer):
        if answer:
            self.installSelected()

    def installSelected(self):
        idx = self["list"].getSelectedIndex()
        if idx < len(self.panels):
            cmd = self.panels[idx][1]
            self.session.open(Console, "Installing Panel", [cmd])
    
    def restartGUI(self):
        self.session.open(TryQuitMainloop, 3)


class PluginsPanel(Screen):
    def __init__(self, session):
        Screen.__init__(self, session)
        self.skin = """
        <screen position="100,center" size="800,900" title="Plugins Manager">
            <ePixmap position="0,0" size="800,900" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EmilPanelPro/images/back.png" zPosition="-1" />
            <widget source="title" render="Label" 
                position="50,30" size="700,60"
                font="Regular;50" halign="center" valign="center" 
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget name="list" position="50,110" size="700,680" 
                itemHeight="68" scrollbarMode="showOnDemand"
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget source="key_red" render="Label" position="50,820" size="200,50"
                backgroundColor="#9f1313" 
                halign="center" valign="center" font="Regular;32" 
                foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_green" render="Label" position="300,820" size="200,50"
                backgroundColor="#1f771f" 
                halign="center" valign="center" font="Regular;32" 
                foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_blue" render="Label" position="550,820" size="200,50"
                backgroundColor="#18188b" 
                halign="center" valign="center" font="Regular;32" 
                foregroundColor="#ffffff" zPosition="1"/>
        </screen>"""
        
        self["title"] = StaticText("Plugins Manager")
        self["list"] = MenuList([])
        self["key_red"] = StaticText("Back")
        self["key_green"] = StaticText("Install")
        self["key_blue"] = StaticText("Restart")
        
        self["actions"] = ActionMap(["ColorActions", "OkCancelActions"], {
            "ok": self.confirmInstall,
            "cancel": self.close,
            "red": self.close,
            "green": self.confirmInstall,
            "blue": self.restartGUI
        }, -1)
        
        self.plugins = [
            ("ArabicSavior", "wget http://dreambox4u.com/emilnabil237/plugins/ArabicSavior/installer.sh -O - | /bin/sh"),
            ("Alajre", "wget https://dreambox4u.com/emilnabil237/plugins/alajre/installer.sh -O - | /bin/sh"),
            ("Ansite", "wget https://raw.githubusercontent.com/emil237/ansite/refs/heads/main/installer.sh -O - | /bin/sh"),
            ("Apod", "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/apod/installer.sh -O - | /bin/sh"),
            ("Apsattv", "wget https://raw.githubusercontent.com/Belfagor2005/Apsattv/main/installer.sh -O - | /bin/sh"),
            ("Astronomy", "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/astronomy/installer.sh -O - | /bin/sh"),
            ("Athan Times", "wget https://dreambox4u.com/emilnabil237/plugins/athantimes/installer.sh -O - | /bin/sh"),
            ("Atilehd", "wget https://dreambox4u.com/emilnabil237/plugins/atilehd/installer.sh -O - | /bin/sh"),
            ("Azkar Almuslim", "wget https://dreambox4u.com/emilnabil237/plugins/azkar-almuslim/installer.sh -O - | /bin/sh"),
            ("Backupflashe", "wget https://raw.githubusercontent.com/fairbird/backupflash/main/installer.sh -O - | /bin/sh"),
            ("BootlogoSwap-Dreambox", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/bootlogoswaper-dreambox.sh -O - | /bin/sh"),
            ("BootlogoSwap-Gemini", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/bootlogoswaper-gemini.sh -O - | /bin/sh"),
            ("BootlogoSwap-Merlin", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/BootlogoSwap-Merlin.sh -O - | /bin/sh"),
            ("BootlogoSwap-TS", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/bootlogoswaper-ts.sh -O - | /bin/sh"),
            ("BissFeedAutoKey", "wget https://raw.githubusercontent.com/emilnabil/bissfeed-autokey/main/installer.sh -O - | /bin/sh"),
            ("Bootvideo", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/Bootvideo.sh -O - | /bin/sh"),
            ("CacheFlush", "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/cacheflush/cacheflush.sh -O - | /bin/sh"),
            ("CCcaminfo", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/cccaminfo.sh -O - | /bin/sh"),
            ("channelselectionplus", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/channelselectionplus.sh -O - | /bin/sh"),
            ("CrondManager", "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/crondmanager/installer.sh -O - | /bin/sh"),
            ("chocholousek-picons", "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/chocholousek-picons.sh -O - | /bin/sh"),
            ("CrashLogoViewer", "wget https://dreambox4u.com/emilnabil237/plugins/crashlogviewer/install-CrashLogViewer.sh -O - | /bin/sh"),
            ("CrondManger", "wget https://github.com/emil237/download-plugins/raw/main/cronmanager.sh -O - | /bin/sh"),
            ("DisplaySkin", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/displayskin.sh -O - | /bin/sh"),
            ("Epg Grabber", "wget https://dreambox4u.com/emilnabil237/plugins/Epg-Grabber/installer.sh -O - | /bin/sh"),
            ("EPGImport", "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/epgimport.sh -O - | /bin/sh"),
            ("EPGImport-99", "wget https://raw.githubusercontent.com/Belfagor2005/EPGImport-99/main/installer.sh -O - | /bin/sh"),
            ("EPGTranslator", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/epgtranslatorlite.sh -O - | /bin/sh"),
            ("Estalker", "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/EStalker/EStalker.sh -O - | /bin/sh"),
            ("EventDataManager", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/eventdatamanager.sh -O - | /bin/sh"),
            ("Feeds-Finder", "wget https://dreambox4u.com/emilnabil237/plugins/feeds-finder/installer.sh -O - | /bin/sh"),
            ("Filebrowser", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/filebrowser.sh -O - | /bin/sh"),
            ("Filmxy", "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/filmxy/filmxy.sh -O - | /bin/sh"),
            ("Footonsat", "wget https://dreambox4u.com/emilnabil237/plugins/FootOnsat/installer.sh -O - | /bin/sh"),
            ("Freearhey", "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/freearhey/freearhey.sh -O - | /bin/sh"),
            ("FreeCCcamServer", "wget https://ia803104.us.archive.org/0/items/freecccamserver/installer.sh -O - | /bin/sh"),
            ("HasBahCa", "wget https://dreambox4u.com/emilnabil237/plugins/HasBahCa/installer.sh -O - | /bin/sh"),
            ("HbbTv", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/hbbtv.sh -O - | /bin/sh"),
            ("HistoryZapSelector", "wget https://dreambox4u.com/emilnabil237/plugins/historyzap/installer.sh -O - | /bin/sh"),
            ("InfobarHide", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/infobarhide.sh -O - | /bin/sh"),
            ("Internet-Speedtest", "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/internet-speedtest.sh -O - | /bin/sh"),
            ("IP_Checker", "wget https://raw.githubusercontent.com/emil237/plugins/refs/heads/main/IP_Checker.sh -O - | /bin/sh"),
            ("Iptv-Org-Playlists", "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/iptv-org-playlists/iptv-org-playlists.sh -O - | /bin/sh"),
            ("iptvdream", "wget https://raw.githubusercontent.com/emilnabil/download-plugins/main/iptvdream/iptvdream.sh -O - | /bin/sh"),
            ("IptvPlayer", "wget https://raw.githubusercontent.com/emil237/iptvplayer/main/iptvinstaller.sh -O - | /bin/sh"),
            ("Iptvupdater", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/iptvupdater.sh -O - | /bin/sh"),
            ("KeyAdder", "wget https://raw.githubusercontent.com/fairbird/KeyAdder/main/installer.sh -O - | /bin/sh"),
            ("MerlinSkinThemes", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/merlinskinthemes.sh -O - | /bin/sh"),
            ("levi45-freeserver", "wget https://raw.githubusercontent.com/emil237/plugins/refs/heads/main/levi45-freeserver/levi45-freeserver.sh -O - | /bin/sh"),
            ("levi45-settings", "wget https://dreambox4u.com/emilnabil237/plugins/levi45-settings/levi45-settings.sh -O - | /bin/sh"),
            ("M3uConverter", "wget https://raw.githubusercontent.com/Belfagor2005/Archimede-M3UConverter/main/installer.sh -O - | /bin/sh"),
            ("MmPicons", "wget https://raw.githubusercontent.com/Belfagor2005/mmPicons/main/installer.sh -O - | /bin/sh"),
            ("MoviesManager", "wget http://dreambox4u.com/emilnabil237/plugins/Transmission/MoviesManager.sh -O - | /bin/sh"),
            ("ONEupdater", "wget https://raw.githubusercontent.com/Sat-Club/ONEupdaterE2/main/installer.sh -O - | /bin/sh"),
            ("PluginSort", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/pluginsort.sh -O - | /bin/sh"),
            ("QuickButton", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/quickbutton.sh -O - | /bin/sh"),
            ("Quran-karem", "wget https://dreambox4u.com/emilnabil237/plugins/quran/installer.sh -O - | /bin/sh"),
            ("Quran-karem_v2.2", "wget https://raw.githubusercontent.com/emil237/quran/main/installer.sh -O - | /bin/sh"),
            ("RaedQuickSignal", "wget https://dreambox4u.com/emilnabil237/plugins/RaedQuickSignal/installer.sh -O - | /bin/sh"),
            ("Pauli", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/pauli.sh -O - | /bin/sh"),
            ("Plutotv", "wget https://raw.githubusercontent.com/emilnabil/download-plugins/main/plutotv/plutotv.sh -O - | /bin/sh"),
            ("scriptexecuter", "wget http://dreambox4u.com/emilnabil237/plugins/scriptexecuter/installer.sh -O - | /bin/sh"),
            ("ServiceScanUpdates", "wget https://dreambox4u.com/emilnabil237/plugins/servicescanupdates/servicescanupdates.sh -O - | /bin/sh"),
            ("SimpleZoomPanel", "wget https://raw.githubusercontent.com/Belfagor2005/SimpleZooomPanel/main/installer.sh -O - | /bin/sh"),
            ("skincomponents-extmultilistselection", "curl -kL https://github.com/emilnabil/dreambox/raw/refs/heads/main/skincomponents-extmultilistselection.sh | bash"),
            ("SubsSupport_1.5.8-r9", "wget https://dreambox4u.com/emilnabil237/plugins/SubsSupport/installer1.sh -O - | /bin/sh"),
            ("TheWeather", "wget https://raw.githubusercontent.com/biko-73/TheWeather/main/installer.sh -O - | /bin/sh"),
            ("TMBD", "wget https://raw.githubusercontent.com/biko-73/TMBD/main/installer.sh -O - | /bin/sh"),
            ("TvDream", "wget https://raw.githubusercontent.com/Belfagor2005/tvDream/main/installer.sh -O - | /bin/sh"),
            ("TvManager", "wget https://raw.githubusercontent.com/Belfagor2005/tvManager/main/installer.sh -O - | /bin/sh"),
            ("TvParsa", "wget https://raw.githubusercontent.com/Belfagor2005/tvParsa/main/installer.sh -O - | /bin/sh"),
            ("TvRaiPreview", "wget https://raw.githubusercontent.com/Belfagor2005/tvRaiPreview/main/installer.sh -O - | /bin/sh"),
            ("TvSettings", "wget https://raw.githubusercontent.com/Belfagor2005/tvSettings/main/installer.sh -O - | /bin/sh"),
            ("uninstaller", "curl -kL https://github.com/emilnabil/dreambox/raw/refs/heads/main/uninstaller.sh | bash"),
            ("userscripts", "curl -kL https://github.com/emilnabil/dreambox/raw/refs/heads/main/userscripts.sh | bash"),
            ("vavoo_1.15", "wget https://dreambox4u.com/emilnabil237/plugins/vavoo/installer.sh -O - | /bin/sh"),
            ("WeatherPlugin", "wget https://raw.githubusercontent.com/fairbird/WeatherPlugin/master/installer.sh -O - | /bin/sh"),
            ("Wireguard-Vpn", "wget https://raw.githubusercontent.com/m4dhouse/Wireguard-Vpn/refs/heads/python-3.12/WireGuard.sh -O - | /bin/sh"),
            ("WorldCam", "wget https://raw.githubusercontent.com/Belfagor2005/WorldCam/main/installer.sh -O - | /bin/sh")
        ]
        
        self["list"].setList([name for name, url in self.plugins])
    
    def confirmInstall(self):
        idx = self["list"].getSelectedIndex()
        if idx < len(self.plugins):
            plugin_name = self.plugins[idx][0]
            self.session.openWithCallback(
                self.installConfirmed,
                MessageBox,
                "Do you want to install %s ?" % plugin_name,
                MessageBox.TYPE_YESNO
            )
    
    def installConfirmed(self, answer):
        if answer:
            self.installSelected()
    
    def installSelected(self):
        idx = self["list"].getSelectedIndex()
        if idx < len(self.plugins):
            url = self.plugins[idx][1]
            self.session.open(Console, "Installing Plugin", [url])
    
    def restartGUI(self):
        self.session.open(TryQuitMainloop, 3)


class ChannelsPanel(Screen):
    def __init__(self, session):
        Screen.__init__(self, session)
        self.skin = """
        <screen position="100,center" size="800,900" title="Channels Manager">
            <ePixmap position="0,0" size="800,900" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EmilPanelPro/images/back.png" zPosition="-1" />
            <widget source="title" render="Label" 
                position="50,30" size="700,60"
                font="Regular;50" halign="center" valign="center" 
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget name="list" position="50,110" size="700,680" 
                itemHeight="68" scrollbarMode="showOnDemand"
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget source="key_red" render="Label" position="50,820" size="200,50"
                backgroundColor="#9f1313" 
                halign="center" valign="center" font="Regular;32" 
                foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_green" render="Label" position="300,820" size="200,50"
                backgroundColor="#1f771f" 
                halign="center" valign="center" font="Regular;32" 
                foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_blue" render="Label" position="550,820" size="200,50"
                backgroundColor="#18188b" 
                halign="center" valign="center" font="Regular;32" 
                foregroundColor="#ffffff" zPosition="1"/>
        </screen>"""
        
        self["title"] = StaticText("Channels Manager")
        self["list"] = MenuList([])
        self["key_red"] = StaticText("Back")
        self["key_green"] = StaticText("Install")
        self["key_blue"] = StaticText("Restart")
        
        self["actions"] = ActionMap(["ColorActions", "OkCancelActions"], {
            "ok": self.confirmInstall,
            "cancel": self.close,
            "red": self.close,
            "green": self.confirmInstall,
            "blue": self.restartGUI
        }, -1)
        
        self.channels = [
            ("Ahmed Romeh", "https://raw.githubusercontent.com/emilnabil/channel-romeh/main/installer.sh"),
            ("Hazem-Wahba", "https://raw.githubusercontent.com/emilnabil/channel-hazem-wahba/main/installer.sh"),
            ("Khaled Ali", "https://raw.githubusercontent.com/emilnabil/channel-khaled/main/installer.sh"),
            ("Mohamed Goda", "https://raw.githubusercontent.com/emilnabil/channel-mohamed-goda/main/installer.sh"),
            ("Mohamed-Nasr", "https://raw.githubusercontent.com/emilnabil/channel-mnasr/main/installer.sh"),
            ("Ahmed-Mosaad", "https://raw.githubusercontent.com/emilnabil/Channel-Omar2025/main/installer.sh"),
            ("Tarek Ashry", "https://raw.githubusercontent.com/emilnabil/channel-tarek-ashry/main/installer.sh"),
            ("Elsafty-Tv-Radio-Steaming", "https://dreambox4u.com/emilnabil237/settings/elsafty/installer.sh"),
            ("ciefp-channels-e2-75e-34w", "https://raw.githubusercontent.com/emilnabil/download-plugins/main/ciefp-channels-e2/ciefp-channels-e2-75e-34w.sh"),
            ("Vhaninbal-Motor-70E-45W", "https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/vanenbal-channels/Vhannibal-Motor-70E-45W.sh"),
            ("Tuner_Backup_By-Emil-Nabil", "https://github.com/emilnabil/download-plugins/raw/refs/heads/main/restore-tuner-emil.sh"),
            ("Tuner_Backup_By-M-Goda", "https://github.com/emilnabil/download-plugins/raw/refs/heads/main/restore-tuner-goda.sh")
        ]
        
        self["list"].setList([name for name, url in self.channels])
    
    def confirmInstall(self):
        idx = self["list"].getSelectedIndex()
        if idx < len(self.channels):
            name = self.channels[idx][0]
            self.session.openWithCallback(
                self.installSelected,
                MessageBox,
                "Do you want to install %s?" % name,
                type=MessageBox.TYPE_YESNO
            )

    def installSelected(self, answer):
        if answer:
            idx = self["list"].getSelectedIndex()
            if idx < len(self.channels):
                url = self.channels[idx][1]
                self.session.open(Console, "Installing", ["wget -q %s -O - | /bin/sh" % url])
    
    def restartGUI(self):
        self.session.open(TryQuitMainloop, 3)


class FeedsPanel(Screen):
    def __init__(self, session):
        Screen.__init__(self, session)
        self.skin = """
        <screen position="100,center" size="800,900" title="Feeds Manager">
            <ePixmap position="0,0" size="800,900" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EmilPanelPro/images/back.png" zPosition="-1" />
            <widget source="title" render="Label" position="50,30" size="700,60"
                font="Regular;50" halign="center" valign="center"
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget name="list" position="50,110" size="700,680"
                itemHeight="68" scrollbarMode="showOnDemand"
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget source="key_red" render="Label" position="50,820" size="200,50"
                backgroundColor="#9f1313" halign="center" valign="center"
                font="Regular;32" foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_green" render="Label" position="300,820" size="200,50"
                backgroundColor="#1f771f" halign="center" valign="center"
                font="Regular;32" foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_blue" render="Label" position="550,820" size="200,50"
                backgroundColor="#18188b" halign="center" valign="center"
                font="Regular;32" foregroundColor="#ffffff" zPosition="1"/>
        </screen>"""
        
        self["title"] = StaticText("Feeds Manager")
        self["list"] = MenuList([])
        self["key_red"] = StaticText("Back")
        self["key_green"] = StaticText("Install")
        self["key_blue"] = StaticText("Restart")
        
        self["actions"] = ActionMap(["ColorActions", "OkCancelActions"], {
            "ok": self.confirmInstall,
            "cancel": self.close,
            "red": self.close,
            "green": self.confirmInstall,
            "blue": self.restartGUI
        }, -1)
        
        self.plugins = [
            ("Feed-elite-extra_arm64", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/feed-elite-extra_arm64.sh -O - | /bin/sh"),
            ("Feed-elite-extra_armhf", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/feed-elite-extra_armhf.sh -O - | /bin/sh"),
            ("Feed-elite-extra_mipsel", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/feed-elite-extra_mipsel.sh -O - | /bin/sh"),
            ("Feed-DreamArabia", "wget https://github.com/emilnabil/dream/raw/refs/heads/main/dreamarabia.sh -O - | /bin/sh"),
            ("Feed Gemini for OE2.5", "apt update && wget -O /tmp/geminilocale_all.deb http://download.blue-panel.com/geminilocale_gp42.php && dpkg -i /tmp/geminilocale_all.deb"),
            ("Feed Gemini for OE2.6", "apt update && wget -O /tmp/geminilocale_all.deb http://download.blue-panel.com/geminilocale_gp42.php && apt install -y /tmp/geminilocale_all.deb"),
            ("feed-gutemine", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/feed-gutemine.sh -O - | /bin/sh"),
            ("Feed-Merlin", "wget https://raw.githubusercontent.com/emilnabil/dream/main/feed-merlin-dreambox.sh -O - | /bin/sh")
        ]
        
        self["list"].setList([name for name, cmd in self.plugins])

    def confirmInstall(self):
        idx = self["list"].getSelectedIndex()
        if idx < len(self.plugins):
            name = self.plugins[idx][0]
            self.session.openWithCallback(
                self.installConfirmed,
                MessageBox,
                "Do you want to install %s?" % name,
                type=MessageBox.TYPE_YESNO
            )

    def installConfirmed(self, answer):
        if answer:
            idx = self["list"].getSelectedIndex()
            if idx < len(self.plugins):
                cmd = self.plugins[idx][1]
                self.session.open(Console, "Installing Feed", [cmd])

    def restartGUI(self):
        self.session.open(TryQuitMainloop, 3)


class ToolsPanel(Screen):
    def __init__(self, session):
        Screen.__init__(self, session)
        self.skin = """
        <screen position="100,center" size="800,900" title="Tools Manager">
            <ePixmap position="0,0" size="800,900" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EmilPanelPro/images/back.png" zPosition="-1" />
            <widget source="title" render="Label" 
                position="50,30" size="700,60"
                font="Regular;50" halign="center" valign="center" 
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget name="list" position="50,110" size="700,680" 
                itemHeight="68" scrollbarMode="showOnDemand"
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget source="key_red" render="Label" position="50,820" size="200,50"
                backgroundColor="#9f1313" 
                halign="center" valign="center" font="Regular;32" 
                foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_green" render="Label" position="300,820" size="200,50"
                backgroundColor="#1f771f" 
                halign="center" valign="center" font="Regular;32" 
                foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_blue" render="Label" position="550,820" size="200,50"
                backgroundColor="#18188b" 
                halign="center" valign="center" font="Regular;32" 
                foregroundColor="#ffffff" zPosition="1"/>
        </screen>"""
        
        self["title"] = StaticText("Tools Manager")
        self["list"] = MenuList([])
        self["key_red"] = StaticText("Back")
        self["key_green"] = StaticText("Run")
        self["key_blue"] = StaticText("Restart")
        
        self["actions"] = ActionMap(["ColorActions", "OkCancelActions"], {
            "ok": self.confirmRunTool,
            "cancel": self.close,
            "red": self.close,
            "green": self.confirmRunTool,
            "blue": self.restartGUI
        }, -1)
        
        self.tools = [
            ("Wget", "apt-get update -y && apt-get install -y wget"),
            ("Curl", "apt-get install -y curl"),
            ("Update Enigma2 All Python", "wget https://raw.githubusercontent.com/emil237/updates-enigma/main/update-all-python.sh -O - | /bin/sh"),
            ("Installer plugin from-tmp", "apt-get update && dpkg -i /tmp/*.deb && apt-get -f -y install"),
            ("Super Script", "wget https://raw.githubusercontent.com/emilnabil/dreambox/refs/heads/main/Super_Script-dream.sh -O - | /bin/sh"),
            ("Delete-password", "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/scripts-servise/delete-password.sh -O - | /bin/sh"),
            ("Change-Password-To-root", "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/scripts-servise/change-password-to-root.sh -O - | /bin/sh"),
            ("Epg-Khaled", "wget https://raw.githubusercontent.com/emilnabil/epg-khaled/main/EPG-khaled.sh -O - | /bin/sh"),
            ("dream-elite-panel", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/dream-elite-panel.sh -O - | /bin/sh"),
            ("FORMAT_HDD_TO-Ext4", "wget https://raw.githubusercontent.com/emil237/scripts/refs/heads/main/format-hdd.sh -O - | /bin/sh"),
            ("Repair-Inodes-From-Hdd", "wget https://raw.githubusercontent.com/emil237/scripts/refs/heads/main/repair-hdd.sh -O - | /bin/sh"),
            ("Set_Time_NTP-Google", "wget https://dreambox4u.com/emilnabil237/script/set_time.sh -O - | /bin/sh"), 
            ("UpdateSatellitesOealliance", "wget https://raw.githubusercontent.com/emilnabil/download-plugins/refs/heads/main/Satellites-Oealliance.sh -O - | /bin/sh"), 
            ("UpdateSatellitesOpenPli", "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/satellites-openpli.sh -O - | /bin/sh")
        ]
        
        self["list"].setList([name for name, cmd in self.tools])
    
    def confirmRunTool(self):
        idx = self["list"].getSelectedIndex()
        if idx < len(self.tools):
            name = self.tools[idx][0]
            self.session.openWithCallback(
                self.runToolConfirmed,
                MessageBox,
                "Do you want to run %s?" % name,
                type=MessageBox.TYPE_YESNO
            )

    def runToolConfirmed(self, answer):
        if answer:
            idx = self["list"].getSelectedIndex()
            if idx < len(self.tools):
                cmd = self.tools[idx][1]
                self.session.open(Console, "Running Tool", [cmd])
    
    def restartGUI(self):
        self.session.open(TryQuitMainloop, 3)


class SystemPluginsPanel(Screen):
    def __init__(self, session):
        Screen.__init__(self, session)
        self.skin = """
        <screen position="100,center" size="800,900" title="Plugins Manager">
            <ePixmap position="0,0" size="800,900" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EmilPanelPro/images/back.png" zPosition="-1" />
            <widget source="title" render="Label" 
                position="50,30" size="700,60"
                font="Regular;50" halign="center" valign="center" 
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget name="list" position="50,110" size="700,680" 
                itemHeight="68" scrollbarMode="showOnDemand"
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget source="key_red" render="Label" position="50,820" size="200,50"
                backgroundColor="#9f1313" 
                halign="center" valign="center" font="Regular;32" 
                foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_green" render="Label" position="300,820" size="200,50"
                backgroundColor="#1f771f" 
                halign="center" valign="center" font="Regular;32" 
                foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_blue" render="Label" position="550,820" size="200,50"
                backgroundColor="#18188b" 
                halign="center" valign="center" font="Regular;32" 
                foregroundColor="#ffffff" zPosition="1"/>
        </screen>"""
        
        self["title"] = StaticText("System Plugins")
        self["list"] = MenuList([])
        self["key_red"] = StaticText("Back")
        self["key_green"] = StaticText("Install")
        self["key_blue"] = StaticText("Restart")
        
        self["actions"] = ActionMap(["ColorActions", "OkCancelActions"], {
            "ok": self.confirmInstall,
            "cancel": self.close,
            "red": self.close,
            "green": self.confirmInstall,
            "blue": self.restartGUI
        }, -1)
        
        self.plugins = [
            ("AutomaticCleanup", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/AutomaticCleanup.sh -O - | /bin/sh"),
            ("autoresolution_armhf", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/autoresolution_armhf.sh -O - | /bin/sh"),
            ("automaticvolumeadjustment_armhf", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/automaticvolumeadjustment_armhf.sh -O - | /bin/sh"),
            ("Disk_and_CPU_Temperature", "wget https://raw.githubusercontent.com/emilnabil/dreambox/refs/heads/main/disk_and_cpu_temperature.sh -O - | /bin/sh"),
            ("extnumberzap", "wget https://dreambox4u.com/emilnabil237/plugins/extnumberzap/extnumberzap.sh -O - | /bin/sh"),
            ("CrashlogAutoSubmit", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/CrashlogAutoSubmit.sh -O - | /bin/sh"),
            ("DynamicDisplay", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/dynamicdisplay.sh -O - | /bin/sh"),
            ("GeminiAddonManager", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/geminiaddonmanager.sh -O - | /bin/sh"),
            ("GeminiBluePanel", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/geminibluepanel.sh -O - | /bin/sh"),
            ("GeminiHwManager", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/geminihwmanager.sh -O - | /bin/sh"),
            ("GeminiImageBackup", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/geminiimagebackup.sh -O - | /bin/sh"),
            ("MenuSort", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/MenuSort.sh -O - | /bin/sh"),
            ("PluginHider", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/PluginHider.sh -O - | /bin/sh"),
            ("RemoteControlSelection", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/RemoteControlSelection.sh -O - | /bin/sh"),
            ("Satfinder", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/Satfinder.sh -O - | /bin/sh"),
            ("SetPasswd", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/SetPasswd.sh -O - | /bin/sh"),
            ("SkinSelector", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/SkinSelector.sh -O - | /bin/sh"),
            ("Styles", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/styles.sh -O - | /bin/sh"),
            ("SoftwareManager", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/SoftwareManager.sh -O - | /bin/sh"),
            ("StartUpService", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/StartUpService.sh -O - | /bin/sh")
        ]
        
        self["list"].setList([name for name, url in self.plugins])
    
    def confirmInstall(self):
        idx = self["list"].getSelectedIndex()
        if idx < len(self.plugins):
            name = self.plugins[idx][0]
            self.session.openWithCallback(
                self.installConfirmed,
                MessageBox,
                "Do you want to install %s?" % name,
                type=MessageBox.TYPE_YESNO
            )

    def installConfirmed(self, answer):
        if answer:
            idx = self["list"].getSelectedIndex()
            if idx < len(self.plugins):
                url = self.plugins[idx][1]
                self.session.open(Console, "Installing Plugin", [url])
    
    def restartGUI(self):
        self.session.open(TryQuitMainloop, 3)


class MediaPanel(Screen):
    def __init__(self, session):
        Screen.__init__(self, session)
        self.skin = """
        <screen position="100,center" size="800,900" title="Media Manager">
            <ePixmap position="0,0" size="800,900" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EmilPanelPro/images/back.png" zPosition="-1" />
            <widget source="title" render="Label" 
                position="50,30" size="700,60"
                font="Regular;50" halign="center" valign="center" 
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget name="list" position="50,110" size="700,680" 
                itemHeight="68" scrollbarMode="showOnDemand"
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget source="key_red" render="Label" position="50,820" size="200,50"
                backgroundColor="#9f1313" 
                halign="center" valign="center" font="Regular;32" 
                foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_green" render="Label" position="300,820" size="200,50"
                backgroundColor="#1f771f" 
                halign="center" valign="center" font="Regular;32" 
                foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_blue" render="Label" position="550,820" size="200,50"
                backgroundColor="#18188b" 
                halign="center" valign="center" font="Regular;32" 
                foregroundColor="#ffffff" zPosition="1"/>
        </screen>"""

        self["title"] = StaticText("Media Manager")
        self["list"] = MenuList([])
        self["key_red"] = StaticText("Back")
        self["key_green"] = StaticText("Install")
        self["key_blue"] = StaticText("Restart")
        
        self["actions"] = ActionMap(["ColorActions", "OkCancelActions"], {
            "ok": self.confirmInstall,
            "cancel": self.close,
            "red": self.close,
            "green": self.confirmInstall,
            "blue": self.restartGUI
        }, -1)
        
        self.Media = [
            ("BouquetMakerXtream", "wget http://dreambox4u.com/emilnabil237/plugins/BouquetMakerXtream/installer.sh -O - | /bin/sh"),
            ("dreamxtream-dm-900-920", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/dreamxtream-dm-900-920.sh -O - | /bin/sh"),
            ("dreamxtream-dm-1-2", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/dreamxtream-dm-2.sh -O - | /bin/sh"),
            ("dreamxtream-dm-520", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/dreamxtream-dm-520.sh -O - | /bin/sh"),
            ("E2Player-MAXBAMBY", "wget https://gitlab.com/maxbambi/e2iplayer/-/raw/master/install-e2iplayer.sh -O - | /bin/sh"),
            ("E2Player-ZADMARIO", "wget https://gitlab.com/zadmario/e2iplayer/-/raw/master/install-e2iplayer.sh -O - | /bin/sh"),
            ("E2m3ubouquet", "wget https://dreambox4u.com/emilnabil237/plugins/e2m3u2bouquet/installer.sh -O - | /bin/sh"),
            ("ipaudio", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/ipaudio-6.6.sh -O - | /bin/sh"),
            ("iptosat", "wget https://dreambox4u.com/emilnabil237/plugins/iptosat/installer.sh -O - | /bin/sh"),
            ("JediEpgExtream", "wget https://dreambox4u.com/emilnabil237/plugins/jediepgextream/installer.sh -O - | /bin/sh"),
            ("jedimakerxtream", "wget https://dreambox4u.com/emilnabil237/plugins/jedimakerxtream/installer.sh -O - | /bin/sh"),
            ("multistalker", "wget https://dreambox4u.com/emilnabil237/plugins/multistalker/installer.sh -O - | /bin/sh"),
            ("Radio-80-s", "wget https://raw.githubusercontent.com/Belfagor2005/Radio-80-s/main/installer.sh -O - | /bin/sh"),
            ("RadioGit", "wget https://dreambox4u.com/emilnabil237/plugins/radiogit/radiogit.sh -O - | /bin/sh"),
            ("Radiom", "wget https://raw.githubusercontent.com/emilnabil/download-plugins/main/radiom/radiom.sh -O - | /bin/sh"),
            ("Rakutentv", "wget https://raw.githubusercontent.com/emilnabil/download-plugins/main/rakutentv/rakutentv.sh -O - | /bin/sh"),
            ("Tsmedia", "wget -O /tmp/tsmedia.deb https://github.com/emilnabil/dreambox/raw/refs/heads/main/tsmedia.deb && dpkg -i /tmp/tsmedia.deb && sleep 2 && apt-get -f -y install"),
            ("Youtube", "wget https://raw.githubusercontent.com/fairbird/Youtube-Opensource-DreamOS/master/installer.sh -O - | /bin/sh"),
            ("xklass-iptv", "wget https://dreambox4u.com/emilnabil237/plugins/xklass/installer.sh -O - | /bin/sh"),
            ("Xtreamty", "wget https://dreambox4u.com/emilnabil237/plugins/xtreamity/installer.sh -O - | /bin/sh")
        ]
        
        self["list"].setList([name for name, cmd in self.Media])  
    
    def confirmInstall(self):
        idx = self["list"].getSelectedIndex()
        if idx < len(self.Media):
            plugin_name = self.Media[idx][0]
            self.session.openWithCallback(
                self.installConfirmed,
                MessageBox,
                _("Do you want to install %s ?") % plugin_name,
                MessageBox.TYPE_YESNO
            )

    def installConfirmed(self, answer):
        if answer:
            self.installSelected()

    def installSelected(self):
        idx = self["list"].getSelectedIndex()
        if idx < len(self.Media):
            cmd = self.Media[idx][1]
            self.session.open(Console, "Installing Plugin", [cmd])
    
    def restartGUI(self):
        self.session.open(TryQuitMainloop, 3)

        
class MultibootPanel(Screen):
    def __init__(self, session):
        Screen.__init__(self, session)
        self.skin = """
        <screen position="100,center" size="800,900" title="Multiboot Manager">
            <ePixmap position="0,0" size="800,900" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EmilPanelPro/images/back.png" zPosition="-1" />
            <widget source="title" render="Label" 
                position="50,30" size="700,60"
                font="Regular;50" halign="center" valign="center" 
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget name="list" position="50,110" size="700,680" 
                itemHeight="68" scrollbarMode="showOnDemand"
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget source="key_red" render="Label" position="50,820" size="200,50"
                backgroundColor="#9f1313" 
                halign="center" valign="center" font="Regular;32" 
                foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_green" render="Label" position="300,820" size="200,50"
                backgroundColor="#1f771f" 
                halign="center" valign="center" font="Regular;32" 
                foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_blue" render="Label" position="550,820" size="200,50"
                backgroundColor="#18188b" 
                halign="center" valign="center" font="Regular;32" 
                foregroundColor="#ffffff" zPosition="1"/>
        </screen>"""

        self["title"] = StaticText("Multiboot Manager")
        self["list"] = MenuList([])
        self["key_red"] = StaticText("Back")
        self["key_green"] = StaticText("Install")
        self["key_blue"] = StaticText("Restart")
        
        self["actions"] = ActionMap(["ColorActions", "OkCancelActions"], {
            "ok": self.confirmInstall,
            "cancel": self.close,
            "red": self.close,
            "green": self.confirmInstall,
            "blue": self.restartGUI
        }, -1)
        
        self.panels = [
            
  ("Alanturing", "wget -q --no-check-certificate https://github.com/emilnabil/dreambox/raw/refs/heads/main/alanturing.sh -O - | /bin/sh"),          ("Barryallen_12.91-r2-MOD-RAED", "wget -q --no-check-certificate https://dreambox4u.com/emilnabil237/dream/barryallen.sh -O - | /bin/sh"),
            ("Multiboot-Selector", "wget https://github.com/emilnabil/dreambox/raw/refs/heads/main/installer-multiboot-selector.sh -O - | /bin/sh")
        ]
        
        self["list"].setList([name for name, cmd in self.panels])  

    def confirmInstall(self):
        idx = self["list"].getSelectedIndex()
        if idx < len(self.panels):
            name = self.panels[idx][0]
            self.session.openWithCallback(
                self.installConfirmed,
                MessageBox,
                "Do you want to install %s?" % name,
                type=MessageBox.TYPE_YESNO
            )

    def installConfirmed(self, answer):
        if answer:
            idx = self["list"].getSelectedIndex()
            if idx < len(self.panels):
                cmd = self.panels[idx][1]
                self.session.open(Console, "Installing Panel", [cmd])
    
    def restartGUI(self):
        self.session.open(TryQuitMainloop, 3)
        

class SoftcamsPanel(Screen):
    def __init__(self, session):
        Screen.__init__(self, session)
        self.skin = """
        <screen position="100,center" size="800,900" title="Softcams Manager">
            <ePixmap position="0,0" size="800,900" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EmilPanelPro/images/back.png" zPosition="-1" />
            <widget source="title" render="Label" position="50,30" size="700,60"
                font="Regular;50" halign="center" valign="center"
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget name="list" position="50,110" size="700,680"
                itemHeight="68" scrollbarMode="showOnDemand"
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget source="key_red" render="Label" position="50,820" size="200,50"
                backgroundColor="#9f1313" halign="center" valign="center"
                font="Regular;32" foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_green" render="Label" position="300,820" size="200,50"
                backgroundColor="#1f771f" halign="center" valign="center"
                font="Regular;32" foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_blue" render="Label" position="550,820" size="200,50"
                backgroundColor="#18188b" halign="center" valign="center"
                font="Regular;32" foregroundColor="#ffffff" zPosition="1"/>
        </screen>"""
        self["title"] = StaticText("Softcams Manager")
        self["list"] = MenuList([])
        self["key_red"] = StaticText("Back")
        self["key_green"] = StaticText("Install")
        self["key_blue"] = StaticText("Restart")
        self["actions"] = ActionMap(["ColorActions", "OkCancelActions"], {
            "ok": self.confirmInstall,
            "cancel": self.close,
            "red": self.close,
            "green": self.confirmInstall,
            "blue": self.restartGUI
        }, -1)

        self.softcams = [
            ("Cccam", "wget https://dreambox4u.com/emilnabil237/emu/installer-cccam.sh -O - | /bin/sh"),
            ("gosatplus-ncam", "wget https://dreambox4u.com/emilnabil237/emu/installer-gosatplus-ncam.sh -O - | /bin/sh"),
            ("gosatplus-oscam", "wget https://dreambox4u.com/emilnabil237/emu/installer-gosatplus-oscam.sh -O - | /bin/sh"),
            ("gosatplus_v3_arm", "wget http://e2.gosatplus.com/Plugin/V3/arm-openpli-installer_py3_v3.sh -O - | /bin/sh"),
            ("gosatplus_v3_mips", "wget http://e2.gosatplus.com/Plugin/V3/mips-openpli-installer_py3_v3.sh -O - | /bin/sh"),
            ("gosatplus_v3_Fix", "wget http://e2.gosatplus.com/Plugin/V3/GosatPlusPluginFixPy.sh -O - | /bin/sh"),
            ("Hold-flag-ncam", "wget https://dreambox4u.com/emilnabil237/script/Hold-flag-ncam.sh -O - | /bin/sh"),
            ("Hold-flag-Oscam", "wget https://dreambox4u.com/emilnabil237/script/Hold-flag-Oscam.sh -O - | /bin/sh"),
            ("Ncam", "wget https://dreambox4u.com/emilnabil237/emu/installer-ncam.sh -O - | /bin/sh"),
            ("Oscam", "wget https://dreambox4u.com/emilnabil237/emu/installer-oscam.sh -O - | /bin/sh"),
            ("Oscam-11.726-by-lenuxsat", "wget https://dreambox4u.com/emilnabil237/emu/oscam-by-lenuxsat/installer.sh -O - | /bin/sh"),
            ("oscamicam", "wget https://dreambox4u.com/emilnabil237/emu/installer-oscamicam.sh -O - | /bin/sh"),
            ("powercam_v2-icam-arm", "wget https://dreambox4u.com/emilnabil237/emu/powercam/installer.sh -O - | /bin/sh"),
            ("powercam-Ncam", "wget https://dreambox4u.com/emilnabil237/emu/installer-powercam-ncam.sh -O - | /bin/sh"),
            ("powercam-Oscam", "wget https://dreambox4u.com/emilnabil237/emu/installer-powercam-oscam.sh -O - | /bin/sh"),
            ("Restore-flag-ncam", "wget https://dreambox4u.com/emilnabil237/script/Restore-flag-ncam.sh -O - | /bin/sh"),
            ("Restore-flag-oscam", "wget https://dreambox4u.com/emilnabil237/script/Restore-flag-Oscam.sh -O - | /bin/sh"),
            ("Revcam-Ncam", "wget https://dreambox4u.com/emilnabil237/emu/installer-revcam-ncam.sh -O - | /bin/sh"),
            ("Revcam-Oscam", "wget https://dreambox4u.com/emilnabil237/emu/installer-revcam-oscam.sh -O - | /bin/sh"),
            ("Revcam", "wget https://dreambox4u.com/emilnabil237/emu/installer-revcam.sh -O - | /bin/sh"),
            ("Supcam-Ncam", "wget https://dreambox4u.com/emilnabil237/emu/installer-supcam-ncam.sh -O - | /bin/sh"),
            ("Supcam-Oscam", "wget https://dreambox4u.com/emilnabil237/emu/installer-supcam-oscam.sh -O - | /bin/sh"),
            ("Ultracam-Ncam", "wget https://dreambox4u.com/emilnabil237/emu/installer-ultracam-ncam.sh -O - | /bin/sh"),
            ("Ultracam-Oscam", "wget https://dreambox4u.com/emilnabil237/emu/installer-ultracam-oscam.sh -O - | /bin/sh"),
            ("Ultracam", "wget https://dreambox4u.com/emilnabil237/emu/installer-ultracam.sh -O - | /bin/sh")
        ]
        self["list"].setList([name for name, cmd in self.softcams])

    def confirmInstall(self):
        idx = self["list"].getSelectedIndex()
        if idx < len(self.softcams):
            name = self.softcams[idx][0]
            self.session.openWithCallback(
                self.installConfirmed,
                MessageBox,
                "Do you want to install %s?" % name,
                type=MessageBox.TYPE_YESNO
            )

    def installConfirmed(self, answer):
        if answer:
            idx = self["list"].getSelectedIndex()
            if idx < len(self.softcams):
                cmd = self.softcams[idx][1]
                self.session.open(Console, "Installing Softcam", [cmd])

    def restartGUI(self):
        self.session.open(TryQuitMainloop, 3)
        

class BackupPanel(Screen):
    def __init__(self, session):
        Screen.__init__(self, session)
        self.skin = """
        <screen position="100,center" size="800,900" title="Backup Manager">
            <ePixmap position="0,0" size="800,900" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EmilPanelPro/images/back.png" zPosition="-1" />
            <widget source="title" render="Label" position="50,30" size="700,60"
                font="Regular;50" halign="center" valign="center"
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget name="list" position="50,110" size="700,680"
                itemHeight="68" scrollbarMode="showOnDemand"
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget source="key_red" render="Label" position="50,820" size="200,50"
                backgroundColor="#9f1313" halign="center" valign="center"
                font="Regular;32" foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_green" render="Label" position="300,820" size="200,50"
                backgroundColor="#1f771f" halign="center" valign="center"
                font="Regular;32" foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_blue" render="Label" position="550,820" size="200,50"
                backgroundColor="#18188b" halign="center" valign="center"
                font="Regular;32" foregroundColor="#ffffff" zPosition="1"/>
        </screen>"""
        self["title"] = StaticText("Backup Manager")
        self["list"] = MenuList([])
        self["key_red"] = StaticText("Back")
        self["key_green"] = StaticText("Backup")
        self["key_blue"] = StaticText("Restart")
        self["actions"] = ActionMap(["ColorActions", "OkCancelActions"], {
            "ok": self.confirmBackup,
            "cancel": self.close,
            "red": self.close,
            "green": self.confirmBackup,
            "blue": self.restartGUI
        }, -1)

        self.backups = [
            ("Backup-my-Channels", "wget http://dreambox4u.com/emilnabil237/script/Create-My-backup-shannels.sh -O - | /bin/sh"),
            ("Backup-hotkey", "wget http://dreambox4u.com/emilnabil237/script/backup-hotkey.sh -O - | /bin/sh"),
            ("Backup-network", "wget http://dreambox4u.com/emilnabil237/script/backup-network.sh -O - | /bin/sh"),
            ("Backup-softcams", "wget http://dreambox4u.com/emilnabil237/script/backup-softcams.sh -O - | /bin/sh"),
            ("Backup-tuner", "wget http://dreambox4u.com/emilnabil237/script/backup-tuner.sh -O - | /bin/sh"),
            ("Backup-my-bouquetmakerxtream", "wget http://dreambox4u.com/emilnabil237/script/backup-my-bouquetmakerxtream.sh -O - | /bin/sh"),
            ("Backup-my-ip2sat-server", "wget http://dreambox4u.com/emilnabil237/script/backup-my-ip2sat-server.sh -O - | /bin/sh"),
            ("Backup-my-ipaudio-server", "wget http://dreambox4u.com/emilnabil237/script/backup-my-ipaudio-server.sh -O - | /bin/sh"),
            ("Backup-my-ipaudiopro-server", "wget http://dreambox4u.com/emilnabil237/script/backup-my-ipaudiopro-server.sh -O - | /bin/sh"),
            ("Backup-my-jediplaylists", "wget http://dreambox4u.com/emilnabil237/script/backup-my-jediplaylists.sh -O - | /bin/sh"),
            ("Backup-my-multistalkerpro", "wget http://dreambox4u.com/emilnabil237/script/backup-my-multistalkerpro.sh -O - | /bin/sh"),
            ("Backup-my-Subtitle-Setting", "wget http://dreambox4u.com/emilnabil237/script/backup_my-subtitle-setting.sh -O - | /bin/sh"),
            ("Backup-my-xstreamity-servers", "wget http://dreambox4u.com/emilnabil237/script/backup-my-xstreamity-servers.sh -O - | /bin/sh"),
            ("Backup-sittings-xtraevent", "wget http://dreambox4u.com/emilnabil237/script/backup-sittings-xtraevent.sh -O - | /bin/sh")
        ]
        self["list"].setList([name for name, cmd in self.backups])

    def confirmBackup(self):
        idx = self["list"].getSelectedIndex()
        if idx < len(self.backups):
            name = self.backups[idx][0]
            self.session.openWithCallback(
                self.backupConfirmed,
                MessageBox,
                "Do you want to create %s?" % name,
                type=MessageBox.TYPE_YESNO
            )

    def backupConfirmed(self, answer):
        if answer:
            idx = self["list"].getSelectedIndex()
            if idx < len(self.backups):
                cmd = self.backups[idx][1]
                self.session.open(Console, "Creating Backup", [cmd])

    def restartGUI(self):
        self.session.open(TryQuitMainloop, 3)


class RestorePanel(Screen):
    def __init__(self, session):
        Screen.__init__(self, session)
        self.skin = """
        <screen position="100,center" size="800,900" title="Restore Manager">
            <ePixmap position="0,0" size="800,900" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EmilPanelPro/images/back.png" zPosition="-1" />
            <widget source="title" render="Label" position="50,30" size="700,60"
                font="Regular;50" halign="center" valign="center"
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget name="list" position="50,110" size="700,680"
                itemHeight="68" scrollbarMode="showOnDemand"
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget source="key_red" render="Label" position="50,820" size="200,50"
                backgroundColor="#9f1313" halign="center" valign="center"
                font="Regular;32" foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_green" render="Label" position="300,820" size="200,50"
                backgroundColor="#1f771f" halign="center" valign="center"
                font="Regular;32" foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_blue" render="Label" position="550,820" size="200,50"
                backgroundColor="#18188b" halign="center" valign="center"
                font="Regular;32" foregroundColor="#ffffff" zPosition="1"/>
        </screen>"""
        self["title"] = StaticText("Restore Manager")
        self["list"] = MenuList([])
        self["key_red"] = StaticText("Back")
        self["key_green"] = StaticText("Restore")
        self["key_blue"] = StaticText("Restart")
        self["actions"] = ActionMap(["ColorActions", "OkCancelActions"], {
            "ok": self.confirmRestore,
            "cancel": self.close,
            "red": self.close,
            "green": self.confirmRestore,
            "blue": self.restartGUI
        }, -1)

        self.restores = [
            ("Restore-my-Channels", "wget http://dreambox4u.com/emilnabil237/script/Restore-My-backup-shannels.sh -O - | /bin/sh"),
            ("Restore-hotkey", "wget http://dreambox4u.com/emilnabil237/script/resore-hotkey.sh -O - | /bin/sh"),
            ("Restore-network", "wget http://dreambox4u.com/emilnabil237/script/restore-network.sh -O - | /bin/sh"),
            ("Restore-softcams", "wget http://dreambox4u.com/emilnabil237/script/restore-softcams.sh -O - | /bin/sh"),
            ("Restore-tuner", "wget http://dreambox4u.com/emilnabil237/script/restore-tuner.sh -O - | /bin/sh"),
            ("Restore-my-bouquetmakerxtream", "wget http://dreambox4u.com/emilnabil237/script/restore-my-bouquetmakerxtream.sh -O - | /bin/sh"),
            ("Restore-my-ip2sat-server", "wget http://dreambox4u.com/emilnabil237/script/restore-my-ip2sat-server.sh -O - | /bin/sh"),
            ("Restore-my-ipaudio-server", "wget http://dreambox4u.com/emilnabil237/script/restore-my-ipaudio-server.sh -O - | /bin/sh"),
            ("Restore-my-ipaudiopro-server", "wget http://dreambox4u.com/emilnabil237/script/restore-my-ipaudiopro-server.sh -O - | /bin/sh"),
            ("Restore-my-jediplaylists", "wget http://dreambox4u.com/emilnabil237/script/restore-my-jediplaylists.sh -O - | /bin/sh"),
            ("Restore-my-multistalkerpro", "wget http://dreambox4u.com/emilnabil237/script/restore-my-multistalkerpro.sh -O - | /bin/sh"),
            ("Restore-My-Subtitle-Setting", "wget http://dreambox4u.com/emilnabil237/script/Restore_my-subtitle-setting.sh -O - | /bin/sh"),
            ("Restore-my-xstreamity-servers", "wget http://dreambox4u.com/emilnabil237/script/restore-my-xstreamity-servers.sh -O - | /bin/sh"),
            ("Restore-sittings-xtraevent", "wget http://dreambox4u.com/emilnabil237/script/restore-sittings-xtraevent.sh -O - | /bin/sh")
        ]
        self["list"].setList([name for name, cmd in self.restores])

    def confirmRestore(self):
        idx = self["list"].getSelectedIndex()
        if idx < len(self.restores):
            name = self.restores[idx][0]
            self.session.openWithCallback(
                self.restoreConfirmed,
                MessageBox,
                "Do you want to restore %s?" % name,
                type=MessageBox.TYPE_YESNO
            )

    def restoreConfirmed(self, answer):
        if answer:
            idx = self["list"].getSelectedIndex()
            if idx < len(self.restores):
                cmd = self.restores[idx][1]
                self.session.open(Console, "Restoring", [cmd])

    def restartGUI(self):
        self.session.open(TryQuitMainloop, 3)


class SkinsPanel(Screen):
    def __init__(self, session):
        Screen.__init__(self, session)
        self.skin = """
        <screen position="100,center" size="800,900" title="Skins Manager">
            <ePixmap position="0,0" size="800,900" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EmilPanelPro/images/back.png" zPosition="-1" />
            <widget source="title" render="Label" position="50,30" size="700,60"
                font="Regular;50" halign="center" valign="center"
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget name="list" position="50,110" size="700,680"
                itemHeight="68" scrollbarMode="showOnDemand"
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget source="key_red" render="Label" position="50,820" size="200,50"
                backgroundColor="#9f1313" halign="center" valign="center"
                font="Regular;32" foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_green" render="Label" position="300,820" size="200,50"
                backgroundColor="#1f771f" halign="center" valign="center"
                font="Regular;32" foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_blue" render="Label" position="550,820" size="200,50"
                backgroundColor="#18188b" halign="center" valign="center"
                font="Regular;32" foregroundColor="#ffffff" zPosition="1"/>
        </screen>"""
        self["title"] = StaticText("Skins Manager")
        self["list"] = MenuList([])
        self["key_red"] = StaticText("Back")
        self["key_green"] = StaticText("Install")
        self["key_blue"] = StaticText("Restart")
        self["actions"] = ActionMap(["ColorActions", "OkCancelActions"], {
            "ok": self.confirmInstall,
            "cancel": self.close,
            "red": self.close,
            "green": self.confirmInstall,
            "blue": self.restartGUI
        }, -1)

        self.skins = [
            ("metrix-HD-oe2.2", "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/skins-for-dreambox/metrix-hd-oe2.2.sh -O - | /bin/sh"),
            ("Brushedalu-HD", "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/skins-for-dreambox/Brushedalu-HD.sh -O - | /bin/sh"),
            ("HoloFHD-Black", "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/skins-for-dreambox/HoloFHD-Black.sh -O - | /bin/sh"),
            ("UltraViolet-HD", "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/skins-for-dreambox/UltraViolet.sh -O - | /bin/sh"),
            ("Vali-HD-atlantis", "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/skins-for-dreambox/Vali-HD-atlantis.sh -O - | /bin/sh"),
            ("Vali-HD-Nano", "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/skins-for-dreambox/Vali-HD-Nano.sh -O - | /bin/sh"),
            ("Vali-HD-Warp", "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/skins-for-dreambox/Vali-HD-Warp.sh -O - | /bin/sh"),
            ("YADS-HD", "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/skins-for-dreambox/YADS-HD.sh -O - | /bin/sh"),
            ("gp4-skin-meridian-fhd", "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/skins-for-dreambox/gp4-skin-meridian-fhd.sh -O - | /bin/sh"),
            ("hdsuisse.one4all.fhd", "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/skins-for-dreambox/hdsuisse.one4all.fhd.sh -O - | /bin/sh"),
            ("My-Flow", "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/skins-for-dreambox/My-Flow.sh -O - | /bin/sh"),
            ("Zombi-Shadow-FHD", "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/skins-for-dreambox/Zombi-Shadow-FHD.sh -O - | /bin/sh"),
            ("ZSkin-FHD", "wget https://github.com/emilnabil/download-plugins/raw/refs/heads/main/skins-for-dreambox/ZSkin-FHD.sh -O - | /bin/sh")
        ]
        self["list"].setList([name for name, cmd in self.skins])

    def confirmInstall(self):
        idx = self["list"].getSelectedIndex()
        if idx < len(self.skins):
            name = self.skins[idx][0]
            self.session.openWithCallback(
                self.installConfirmed,
                MessageBox,
                "Do you want to install %s?" % name,
                type=MessageBox.TYPE_YESNO
            )

    def installConfirmed(self, answer):
        if answer:
            idx = self["list"].getSelectedIndex()
            if idx < len(self.skins):
                cmd = self.skins[idx][1]
                self.session.open(Console, "Installing Skin", [cmd])

    def restartGUI(self):
        self.session.open(TryQuitMainloop, 3)


class RemovePanel(Screen):
    def __init__(self, session):
        Screen.__init__(self, session)
        self.skin = """
        <screen position="100,center" size="800,900" title="Remove Manager">
            <ePixmap position="0,0" size="800,900" pixmap="/usr/lib/enigma2/python/Plugins/Extensions/EmilPanelPro/images/back.png" zPosition="-1" />
            <widget source="title" render="Label" position="50,30" size="700,60"
                font="Regular;50" halign="center" valign="center"
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget name="list" position="50,110" size="700,680"
                itemHeight="68" scrollbarMode="showOnDemand"
                foregroundColor="#ffffff" backgroundColor="#000000" />
            <widget source="key_red" render="Label" position="50,820" size="200,50"
                backgroundColor="#9f1313" halign="center" valign="center"
                font="Regular;32" foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_green" render="Label" position="300,820" size="200,50"
                backgroundColor="#1f771f" halign="center" valign="center"
                font="Regular;32" foregroundColor="#ffffff" zPosition="1"/>
            <widget source="key_blue" render="Label" position="550,820" size="200,50"
                backgroundColor="#18188b" halign="center" valign="center"
                font="Regular;32" foregroundColor="#ffffff" zPosition="1"/>
        </screen>"""
        self["title"] = StaticText("Remove Manager")
        self["list"] = MenuList([])
        self["key_red"] = StaticText("Back")
        self["key_green"] = StaticText("Remove")
        self["key_blue"] = StaticText("Restart")
        self["actions"] = ActionMap(["ColorActions", "OkCancelActions"], {
            "ok": self.confirmRemove,
            "cancel": self.close,
            "red": self.close,
            "green": self.confirmRemove,
            "blue": self.restartGUI
        }, -1)

        self.panels = [
              ("Remove all_Crashlogs", "wget https://dreambox4u.com/emilnabil237/script/remove/DEL_all_Crashlogs.sh -O - | /bin/sh"),
  ("Remove-Ajpanel", "wget https://dreambox4u.com/emilnabil237/script/remove/remove-ajpanel.sh -O - | /bin/sh"),          ("Remove BouquetMakerXtream", "wget https://dreambox4u.com/emilnabil237/script/remove/remove-bouquetmakerxtream.sh -O - | /bin/sh"),
            ("Remove Feed-Dreamarapia", "wget https://raw.githubusercontent.com/emilnabil/dreambox/refs/heads/main/remove-dreamarapia.sh -O - | /bin/sh"),
            ("Remove Feed-geminilocale", "wget https://raw.githubusercontent.com/emilnabil/dreambox/refs/heads/main/remove-geminilocale.sh -O - | /bin/sh"),
            ("Remove Oscam_Supcam", "wget https://dreambox4u.com/emilnabil237/script/remove/del-Oscam_Supcam.sh -O - | /bin/sh"),
            ("Remove CCcamFinder", "wget https://dreambox4u.com/emilnabil237/script/remove/DEL-CCcamFinder.sh -O - | /bin/sh"),
            ("Remove-Channels", "wget https://dreambox4u.com/emilnabil237/script/remove/DEL-channels.sh -O - | /bin/sh"),
            ("Remove-E2iplayer", "wget https://dreambox4u.com/emilnabil237/script/remove/DEL-e2iplayer.sh -O - | /bin/sh"),
            ("Remove-Emu-All", "wget https://dreambox4u.com/emilnabil237/script/remove/DEL-emus.sh -O - | /bin/sh"),
            ("Remove-Emu-Ncam", "wget https://dreambox4u.com/emilnabil237/script/remove/del-emu-ncam.sh -O - | /bin/sh"),
            ("Remove-Emu-Oscam", "wget https://dreambox4u.com/emilnabil237/script/remove/del-emu-oscam.sh -O - | /bin/sh"),
            ("Remove-Emus-Config-Files", "wget https://dreambox4u.com/emilnabil237/script/remove/DEL-emus-config-files.sh -O - | /bin/sh"),
            ("Remove-Jedimaker-playlists", "wget https://dreambox4u.com/emilnabil237/script/remove/del-Jedimaker-playlists.sh -O - | /bin/sh"),
            ("Remove-Plugin-mediaplayer2", "wget https://dreambox4u.com/emilnabil237/script/remove/DEL-mediaplayer2.sh -O - | /bin/sh"),
            ("Remove-Plugin-NetSpeedTest", "wget https://dreambox4u.com/emilnabil237/script/remove/DEL-NetSpeedTest.sh -O - | /bin/sh"),
            ("Remove-Plugin-OscamFinder", "wget https://dreambox4u.com/emilnabil237/script/remove/DEL-OscamFinder.sh -O - | /bin/sh"),
            ("Remove-Plugin-alternativesoftcammanager", "wget https://dreambox4u.com/emilnabil237/script/remove/DEL-plugin-alternativesoftcammanager.sh -O - | /bin/sh"),
            ("Remove-Plugin-Plugin-FreeServer", "wget https://dreambox4u.com/emilnabil237/script/remove/DEL-Plugin-FreeServer.sh -O - | /bin/sh"),
            ("Remove-Plugin-levi45-addonsmanager", "wget https://dreambox4u.com/emilnabil237/script/remove/DEL-plugin-levi45-addonsmanager.sh -O - | /bin/sh"),
            ("Remove-Plugin-m3u-converter", "wget https://dreambox4u.com/emilnabil237/script/remove/DEL-plugin-m3u-converter.sh -O - | /bin/sh"),
            ("Remove-Plugin-SatVenusPANEL", "wget https://dreambox4u.com/emilnabil237/script/remove/DEL-plugin-SatVenusPANEL.sh -O - | /bin/sh"),
            ("Remove-Plugin-tvpanel", "wget https://dreambox4u.com/emilnabil237/script/remove/DEL-plugin-tvpanel.sh -O - | /bin/sh"),
            ("Remove-Plugin-XCplugin", "wget https://dreambox4u.com/emilnabil237/script/remove/DEL-Plugin-XCplugin.sh -O - | /bin/sh"),
            ("Remove-Plugin-Xstreamity", "wget https://dreambox4u.com/emilnabil237/script/remove/DEL-plugin-xstreamity.sh -O - | /bin/sh"),
            ("Remove-Plugin-youtube", "wget https://dreambox4u.com/emilnabil237/script/remove/DEL-plugin-youtube.sh -O - | /bin/sh"),
            ("Remove-Plugin-SoftCam_Manager", "wget https://dreambox4u.com/emilnabil237/script/remove/DEL-SoftCam_Manager.sh -O - | /bin/sh"),
            ("Remove-Plugin-Subssupport", "wget https://dreambox4u.com/emilnabil237/script/remove/DEL-subssupport.sh -O - | /bin/sh"),
            ("Remove-Plugin-Tvpanel", "wget https://dreambox4u.com/emilnabil237/script/remove/DEL-tvpanel.sh -O - | /bin/sh"),
            ("Remove-Tuner-Settings", "wget https://dreambox4u.com/emilnabil237/script/remove/del-Tuner-Settings.sh -O - | /bin/sh"),
            ("Remove-Xstreamity-playlists", "wget https://dreambox4u.com/emilnabil237/script/remove/del-Xstreamity-playlists.sh -O - | /bin/sh")
        ]
        self["list"].setList([name for name, cmd in self.panels])

    def confirmRemove(self):
        idx = self["list"].getSelectedIndex()
        if idx is not None and idx < len(self.panels):
            name = self.panels[idx][0]
            self.session.openWithCallback(
                self.removeConfirmed,
                MessageBox,
                "Do you want to remove %s?" % name,
                type=MessageBox.TYPE_YESNO
            )

    def removeConfirmed(self, answer):
        if answer:
            idx = self["list"].getSelectedIndex()
            if idx is not None and idx < len(self.panels):
                cmd = self.panels[idx][1]
                self.session.open(Console, "Removing Panel", [cmd])

    def restartGUI(self):
        self.session.open(TryQuitMainloop, 3)


def main(session, **kwargs):
    session.open(EmilPanelProScreen)

def menu_main(menuid, **kwargs):
    if menuid == "mainmenu":
        return [(_("EmilPanelPro"), main, "emilpanelpro", 50)]
    return []

def Plugins(path, **kwargs):
    return [
        PluginDescriptor(
            name="FreePanelDMOS",
            description=PLUGIN_DESC,
            where=PluginDescriptor.WHERE_PLUGINMENU,
            icon=resolveFilename(SCOPE_PLUGINS, "Extensions/FreePanelDMOS/FreePanelDMOS.png"),
            fnc=main
        ),
        PluginDescriptor(
            name="FreePanelDMOS",
            description=PLUGIN_DESC,
            where=PluginDescriptor.WHERE_MENU,
            fnc=menu_main,
            icon=resolveFilename(SCOPE_PLUGINS, "Extensions/FreePanelDMOS/FreePanelDMOS.png")
        )
    ]

