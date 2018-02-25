const { app, nativeImage, Menu, Tray } = require('electron')
const path = require('path')
const { getLangpack, isWindows7, isWindows7or8 } = require('./util')
const win = require('./win')
const { isKDE } = require('./linux')

class AppTray {
  constructor() {
    this.savedSettings = {
      notificationsDisabled: false,
      alwaysOnTop: false,
      inAuth: true
    }
    this.updateMenuTimeout = null
    this.tray = null
  }

  create() {
    this.tray = new Tray(this.getDefaultIconPath())
    this.tray.setToolTip('VK Messenger')
    this.tray.setContextMenu(this.getMenu())
    this.tray.on('click', function() {
      let mainWindow = win.getWindow()
      if (!mainWindow) return

      if (mainWindow.isMinimized()) {
        mainWindow.restore()
      } else {
        if (mainWindow.isFocused()) {          
          mainWindow.close()
        }else{          
          mainWindow.show()
        }
      }

      mainWindow.focus()
    })
  }

  destroy() {
    if (this.tray) {
      if (this.updateMenuTimeout) {
        clearTimeout(this.updateMenuTimeout)
        this.updateMenuTimeout = null
      }
      this.tray.destroy()
      this.tray = null
    }
  }

  updateMenu(settings = {}) {
    if (!this.tray) {
      settings = this.getSettings(settings)
      this.savedSettings = settings
      return
    }
    this.tray.setContextMenu(this.getMenu(settings))
  }

  // isFocused() returns `false` immediately after `focus` event, workaround
  updateMenuAsync() {
    clearTimeout(this.updateMenuTimeout)
    this.updateMenuTimeout = setTimeout(() => {
      this.updateMenu()
    })
  }

  isEnabled() {
    return !!this.tray
  }

  setIcon(dataURL) {
    if (!this.tray) {
      return
    }
    this.tray.setImage(this.getImage(dataURL))
  }

  showBalloon() {
    let exeDir = path.dirname(app.getPath('exe'))
    let icon = path.join(exeDir, 'icon48.png')

    let lang = getLangpack()
    let balloonOpts = {
      title: 'VK Messenger',
      content: lang.tray_still_here,
      icon: isWindows7or8() ? null : icon
    }
    this.tray.displayBalloon(balloonOpts)
  }

  getMenu(settings) {
    if (this.updateMenuTimeout) {
      clearTimeout(this.updateMenuTimeout)
      this.updateMenuTimeout = null
    }

    settings = this.getSettings(settings)
    this.savedSettings = settings

    let lang = getLangpack()
    let mainWindow = win.getWindow()

    let template = []
    if (process.platform != 'linux') {
      template.push({
        label: lang.tray_always_on_top,
        type: 'checkbox',
        checked: settings.alwaysOnTop,
        click() {
          win.send('toggle-always-on-top')
        }
      })
    }

    template.push(
      {
        label: lang.tray_disable_notifications,
        type: 'checkbox',
        checked: settings.notificationsDisabled,
        enabled: !settings.inAuth,
        click() {
          win.send('toggle-notifications')
        }
      },
      { type: 'separator' },
      {
        label: lang.tray_settings,
        click() {
          mainWindow.show()
          mainWindow.focus()
          win.send('preferences')
        }
      },
      {
        label: lang.tray_quit,
        click() {
          if (mainWindow) {
            mainWindow.forceClose = true
            mainWindow.close()
            app.exit()
          } else {
            app.exit()
          }
        }
      }
    )

    let vis = isWindowVisible()
    template.unshift(vis ? this.getHideMenuItem() : this.getOpenMenuItem())

    return Menu.buildFromTemplate(template)
  }

  getSettings(settings) {
    return Object.assign(this.savedSettings, settings)
  }

  getOpenMenuItem() {
    let lang = getLangpack()
    let mainWindow = win.getWindow()

    return {
      label: lang.tray_open,
      click() {
        mainWindow.show()
        mainWindow.focus()
      }
    }
  }

  getHideMenuItem() {
    let lang = getLangpack()
    let mainWindow = win.getWindow()

    return {
      label: lang.tray_hide,
      click() {
        mainWindow.close()
      }
    }
  }

  getDefaultIconPath() {
    let exeDir = path.dirname(app.getPath('exe'))
    switch (process.platform) {
      case 'win32':
        return path.join(exeDir, 'tray.ico')

      case 'linux':
        let name = isKDE() ? 'icon24.png' : 'icon256.png'
        return path.join(exeDir, name)

      case 'darwin':
        let res = path.join(path.dirname(exeDir), 'Resources')
        let icon = path.join(res, 'trayTemplate.png')
        return icon
    }
  }

  getImage(dataURL = null) {
    if (!dataURL) {
      return nativeImage.createFromPath(this.getDefaultIconPath())
    } else {
      return nativeImage.createFromDataURL(dataURL)
    }
  }
}

function isWindowVisible() {
  if (process.platform != 'win32' || isWindows7()) {
    return win.getWindow().isVisible() && win.getWindow().isFocused()
  } else {
    return win.getWindow().isVisible() || win.getWindow().isFocused()
  }
}

module.exports = new AppTray()
