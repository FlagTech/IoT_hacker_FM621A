#ifndef _KBDRPTPARSER_H_
#define _KBDRPTPARSER_H_

#include <hidboot.h>
#include <usbhub.h>
#include <Keyboard.h>



// Satisfy the IDE, which needs to see the include statment in the ino too.
#ifdef dobogusinclude
  #include <spi4teensy3.h>
  #include <SPI.h>
#endif

#include <SPI.h>
#include <SD.h>

class KbdRptParser : public KeyboardReportParser{
    public:
        uint8_t _parse(uint8_t key);
        String _getChar(uint8_t key);
        KbdRptParser();
        String Getkey();
    protected:
        void OnControlKeysChanged(uint8_t before, uint8_t after);

        void OnKeyDown	(uint8_t mod, uint8_t key);
        void OnKeyUp	(uint8_t mod, uint8_t key);
        void OnKeyPressed(uint8_t key);
        
        void _press(uint8_t key);
        void _release(uint8_t key);

    private:
        bool shift = false;
        String _key;
};
#endif