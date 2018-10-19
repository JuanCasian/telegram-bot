FROM ubuntu:18.04

MAINTAINER Juan Casian <me@juanpedrocasian.com>

RUN apt-get update && apt-get upgrade -y && \ 
		apt-get install -y vim git curl && \
		curl "https://raw.githubusercontent.com/JuanCasian/Vim-Configuration/master/.vimrc" >> ~/.vimrc && \
		git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim && \
		vim +PluginInstall +qall  && \
		rm ~/.vimrc && curl "https://raw.githubusercontent.com/JuanCasian/Vim-Configuration/master/final" >> ~/.vimrc && \
		apt-get install -y zsh && \
		apt-get install -y build-essential && \
		ZSH=~/.oh-my-zsh && \
		git clone --depth=1 https://github.com/robbyrussell/oh-my-zsh.git "$ZSH" && \
		cp "$ZSH"/templates/zshrc.zsh-template ~/.zshrc && \
		sed "/^export ZSH=/ c export ZSH=\"$ZSH\"" ~/.zshrc > ~/.zshrc-omztemp && \
		mv -f ~/.zshrc-omztemp ~/.zshrc && \
		apt-get install -y python python3 python-pip python3-pip && \
		echo "alias python='python3'" >> ~/.zshrc && \
		mkdir ~/Documents && \
		echo "\033[0;32mALL READY"

CMD cd ~/ && zsh && echo "Welcome"
