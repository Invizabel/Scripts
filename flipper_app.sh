clear

rm -rf ~/Downloads/flipper-application-catalog
rm -rf ~/Downloads/qTemp
rm -rf ~/Downloads/qApps/

mkdir ~/Downloads/qApps/
mkdir ~/Downloads/qTemp

touch ~/Downloads/qApps/errors.log

cd ~/Downloads
git clone https://github.com/flipperdevices/flipper-application-catalog
cd ~/Downloads/flipper-application-catalog/applications

let "count=0"
find -follow | grep .yml| while IFS= read -r line; do
    echo $line
    ((count++))
    if python3 -u ~/Downloads/flipper-application-catalog/tools/bundle.py --nolint $line "bundle_$count.zip" 2>&1 | grep -qi 'error'; then echo $line >> ~/Downloads/qApps/errors.log; fi
done

cp bundle*.zip ~/Downloads/qTemp
cd ~/Downloads/qTemp
find -follow | grep zip | while IFS= read -r line; do
    echo $line
    unzip $line
    cd code
    python3 -m ufbt
    cd dist
    cp *.fap ~/Downloads/qApps/
    cd ..
    cd ..
done

cd ~
rm -rf ~/Downloads/qTemp

rm -rf ~/Downloads/flipper-application-catalog
