rm -rf flipper_venv
python3 -m venv flipper_venv
source flipper_venv/bin/activate

clear

rm -rf ~/Downloads/flipper-application-catalog
rm -rf ~/Downloads/qApps/

mkdir ~/Downloads/qApps
mkdir ~/Downloads/qApps/Bluetooth
mkdir ~/Downloads/qApps/GPIO
mkdir ~/Downloads/qApps/Games
mkdir ~/Downloads/qApps/Infrared
mkdir ~/Downloads/qApps/Media
mkdir ~/Downloads/qApps/NFC
mkdir ~/Downloads/qApps/RFID
mkdir ~/Downloads/qApps/Sub-GHz
mkdir ~/Downloads/qApps/Tools
mkdir ~/Downloads/qApps/USB
mkdir ~/Downloads/qApps/iButton

touch ~/Downloads/qApps/errors.log

cd ~/Downloads
git clone https://github.com/flipperdevices/flipper-application-catalog
pip install -r ~/Downloads/flipper-application-catalog/tools/requirements.txt
cd ~/Downloads/flipper-application-catalog/applications/Bluetooth

let "count=0"
find -follow | grep .yml | while IFS= read -r line; do
    cd ~/Downloads/flipper-application-catalog/applications/Bluetooth
    rm -rf temp
    mkdir temp
    echo $line
    ((count++))
    if python3 -u ~/Downloads/flipper-application-catalog/tools/bundle.py --nolint $line "bundle_$count.zip" 2>&1 | grep -qi 'error'; then echo $line >> ~/Downloads/qApps/errors.log; continue; fi
    cp bundle_$count.zip temp
    cd temp
    unzip ~/Downloads/flipper-application-catalog/applications/Bluetooth/temp/bundle_$count.zip
    cd ~/Downloads/flipper-application-catalog/applications/Bluetooth/temp/code/
    python3 -m ufbt
    cp ~/Downloads/flipper-application-catalog/applications/Bluetooth/temp/code/dist/*.fap ~/Downloads/qApps/Bluetooth
    rm -rf code
done

cd ~/Downloads/flipper-application-catalog/applications/GPIO

let "count=0"
find -follow | grep .yml | while IFS= read -r line; do
    cd ~/Downloads/flipper-application-catalog/applications/GPIO
    rm -rf temp
    mkdir temp
    echo $line
    ((count++))
    if python3 -u ~/Downloads/flipper-application-catalog/tools/bundle.py --nolint $line "bundle_$count.zip" 2>&1 | grep -qi 'error'; then echo $line >> ~/Downloads/qApps/errors.log; continue; fi
    cp bundle_$count.zip temp
    cd temp
    unzip ~/Downloads/flipper-application-catalog/applications/GPIO/temp/bundle_$count.zip
    cd ~/Downloads/flipper-application-catalog/applications/GPIO/temp/code/
    python3 -m ufbt
    cp ~/Downloads/flipper-application-catalog/applications/GPIO/temp/code/dist/*.fap ~/Downloads/qApps/GPIO
    rm -rf code
done

cd ~/Downloads/flipper-application-catalog/applications/Games

let "count=0"
find -follow | grep .yml | while IFS= read -r line; do
    cd ~/Downloads/flipper-application-catalog/applications/Games
    rm -rf temp
    mkdir temp
    echo $line
    ((count++))
    if python3 -u ~/Downloads/flipper-application-catalog/tools/bundle.py --nolint $line "bundle_$count.zip" 2>&1 | grep -qi 'error'; then echo $line >> ~/Downloads/qApps/errors.log; continue; fi
    cp bundle_$count.zip temp
    cd temp
    unzip ~/Downloads/flipper-application-catalog/applications/Games/temp/bundle_$count.zip
    cd ~/Downloads/flipper-application-catalog/applications/Games/temp/code/
    python3 -m ufbt
    cp ~/Downloads/flipper-application-catalog/applications/Games/temp/code/dist/*.fap ~/Downloads/qApps/Games
    rm -rf code
done

cd ~/Downloads/flipper-application-catalog/applications/Infrared

let "count=0"
find -follow | grep .yml | while IFS= read -r line; do
    cd ~/Downloads/flipper-application-catalog/applications/Infrared
    rm -rf temp
    mkdir temp
    echo $line
    ((count++))
    if python3 -u ~/Downloads/flipper-application-catalog/tools/bundle.py --nolint $line "bundle_$count.zip" 2>&1 | grep -qi 'error'; then echo $line >> ~/Downloads/qApps/errors.log; continue; fi
    cp bundle_$count.zip temp
    cd temp
    unzip ~/Downloads/flipper-application-catalog/applications/Infrared/temp/bundle_$count.zip
    cd ~/Downloads/flipper-application-catalog/applications/Infrared/temp/code/
    python3 -m ufbt
    cp ~/Downloads/flipper-application-catalog/applications/Infrared/temp/code/dist/*.fap ~/Downloads/qApps/Infrared
    rm -rf code
done

cd ~/Downloads/flipper-application-catalog/applications/Media

let "count=0"
find -follow | grep .yml | while IFS= read -r line; do
    cd ~/Downloads/flipper-application-catalog/applications/Media
    rm -rf temp
    mkdir temp
    echo $line
    ((count++))
    if python3 -u ~/Downloads/flipper-application-catalog/tools/bundle.py --nolint $line "bundle_$count.zip" 2>&1 | grep -qi 'error'; then echo $line >> ~/Downloads/qApps/errors.log; continue; fi
    cp bundle_$count.zip temp
    cd temp
    unzip ~/Downloads/flipper-application-catalog/applications/Media/temp/bundle_$count.zip
    cd ~/Downloads/flipper-application-catalog/applications/Media/temp/code/
    python3 -m ufbt
    cp ~/Downloads/flipper-application-catalog/applications/Media/temp/code/dist/*.fap ~/Downloads/qApps/Media
    rm -rf code
done

cd ~/Downloads/flipper-application-catalog/applications/NFC

let "count=0"
find -follow | grep .yml | while IFS= read -r line; do
    cd ~/Downloads/flipper-application-catalog/applications/NFC
    rm -rf temp
    mkdir temp
    echo $line
    ((count++))
    if python3 -u ~/Downloads/flipper-application-catalog/tools/bundle.py --nolint $line "bundle_$count.zip" 2>&1 | grep -qi 'error'; then echo $line >> ~/Downloads/qApps/errors.log; continue; fi
    cp bundle_$count.zip temp
    cd temp
    unzip ~/Downloads/flipper-application-catalog/applications/NFC/temp/bundle_$count.zip
    cd ~/Downloads/flipper-application-catalog/applications/NFC/temp/code/
    python3 -m ufbt
    cp ~/Downloads/flipper-application-catalog/applications/NFC/temp/code/dist/*.fap ~/Downloads/qApps/NFC
    rm -rf code
done

cd ~/Downloads/flipper-application-catalog/applications/RFID

let "count=0"
find -follow | grep .yml | while IFS= read -r line; do
    cd ~/Downloads/flipper-application-catalog/applications/RFID
    rm -rf temp
    mkdir temp
    echo $line
    ((count++))
    if python3 -u ~/Downloads/flipper-application-catalog/tools/bundle.py --nolint $line "bundle_$count.zip" 2>&1 | grep -qi 'error'; then echo $line >> ~/Downloads/qApps/errors.log; continue; fi
    cp bundle_$count.zip temp
    cd temp
    unzip ~/Downloads/flipper-application-catalog/applications/RFID/temp/bundle_$count.zip
    cd ~/Downloads/flipper-application-catalog/applications/RFID/temp/code/
    python3 -m ufbt
    cp ~/Downloads/flipper-application-catalog/applications/RFID/temp/code/dist/*.fap ~/Downloads/qApps/RFID
    rm -rf code
done

cd ~/Downloads/flipper-application-catalog/applications/Sub-GHz

let "count=0"
find -follow | grep .yml | while IFS= read -r line; do
    cd ~/Downloads/flipper-application-catalog/applications/Sub-GHz
    rm -rf temp
    mkdir temp
    echo $line
    ((count++))
    if python3 -u ~/Downloads/flipper-application-catalog/tools/bundle.py --nolint $line "bundle_$count.zip" 2>&1 | grep -qi 'error'; then echo $line >> ~/Downloads/qApps/errors.log; continue; fi
    cp bundle_$count.zip temp
    cd temp
    unzip ~/Downloads/flipper-application-catalog/applications/Sub-GHz/temp/bundle_$count.zip
    cd ~/Downloads/flipper-application-catalog/applications/Sub-GHz/temp/code/
    python3 -m ufbt
    cp ~/Downloads/flipper-application-catalog/applications/Sub-GHz/temp/code/dist/*.fap ~/Downloads/qApps/Sub-GHz
    rm -rf code
done

cd ~/Downloads/flipper-application-catalog/applications/Tools

let "count=0"
find -follow | grep .yml | while IFS= read -r line; do
    cd ~/Downloads/flipper-application-catalog/applications/Tools
    rm -rf temp
    mkdir temp
    echo $line
    ((count++))
    if python3 -u ~/Downloads/flipper-application-catalog/tools/bundle.py --nolint $line "bundle_$count.zip" 2>&1 | grep -qi 'error'; then echo $line >> ~/Downloads/qApps/errors.log; continue; fi
    cp bundle_$count.zip temp
    cd temp
    unzip ~/Downloads/flipper-application-catalog/applications/Tools/temp/bundle_$count.zip
    cd ~/Downloads/flipper-application-catalog/applications/Tools/temp/code/
    python3 -m ufbt
    cp ~/Downloads/flipper-application-catalog/applications/Tools/temp/code/dist/*.fap ~/Downloads/qApps/Tools
    rm -rf code
done

cd ~/Downloads/flipper-application-catalog/applications/USB

let "count=0"
find -follow | grep .yml | while IFS= read -r line; do
    cd ~/Downloads/flipper-application-catalog/applications/USB
    rm -rf temp
    mkdir temp
    echo $line
    ((count++))
    if python3 -u ~/Downloads/flipper-application-catalog/tools/bundle.py --nolint $line "bundle_$count.zip" 2>&1 | grep -qi 'error'; then echo $line >> ~/Downloads/qApps/errors.log; continue; fi
    cp bundle_$count.zip temp
    cd temp
    unzip ~/Downloads/flipper-application-catalog/applications/USB/temp/bundle_$count.zip
    cd ~/Downloads/flipper-application-catalog/applications/USB/temp/code/
    python3 -m ufbt
    cp ~/Downloads/flipper-application-catalog/applications/USB/temp/code/dist/*.fap ~/Downloads/qApps/USB
    rm -rf code
done

cd ~/Downloads/flipper-application-catalog/applications/iButton

let "count=0"
find -follow | grep .yml | while IFS= read -r line; do
    cd ~/Downloads/flipper-application-catalog/applications/iButton
    rm -rf temp
    mkdir temp
    echo $line
    ((count++))
    if python3 -u ~/Downloads/flipper-application-catalog/tools/bundle.py --nolint $line "bundle_$count.zip" 2>&1 | grep -qi 'error'; then echo $line >> ~/Downloads/qApps/errors.log; continue; fi
    cp bundle_$count.zip temp
    cd temp
    unzip ~/Downloads/flipper-application-catalog/applications/iButton/temp/bundle_$count.zip
    cd ~/Downloads/flipper-application-catalog/applications/iButton/temp/code/
    python3 -m ufbt
    cp ~/Downloads/flipper-application-catalog/applications/iButton/temp/code/dist/*.fap ~/Downloads/qApps/iButton
    rm -rf code
done

rm -rf ~/Downloads/flipper-application-catalog
rm -rf flipper_venv
