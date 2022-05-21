python3 -m pip install -r requirements.txt
sudo cp duckfetch.py /bin/duckfetch
cd ..
sudo alias duckfetch='python3 /usr/local/bin/duckfetch'
if [ -n "$ZSH_VERSION" ]; then
    echo "zsh detected"
    echo "alias duckfetch='python3 /usr/local/bin/duckfetch'" >> ~/.zshrc
    source ~/.zshrc
else
    echo "bash detected"
    echo "alias duckfetch='python3 /usr/local/bin/duckfetch'" >> ~/.bashrc
    source ~/.bashrc
fi