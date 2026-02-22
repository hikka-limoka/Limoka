echo "1. UserBot | Sekai_Yoneya > запуск..."
cd /home/Sekai_Yoneya/friendly-telegram/ && screen -AmdS -r python3.9 -m friendly-telegram --no-web
echo "2. UserBot | @FORKANI > запуск..."
cd /home/FORKANI/friendly-telegram/ && screen -AmdS -r python3.9 -m friendly-telegram --no-web
echo "Ожидайте! Боты будут запущены в течении минуты!"
