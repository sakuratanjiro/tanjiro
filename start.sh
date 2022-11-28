if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/sakuratanjiro/tanjiro /tanjiro
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /tanjiro
fi
cd /tanjiro
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
