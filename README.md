# eliteracy event auto submit

Why do the same problems 300 times by yourself when you can do it automatically.

## Description

The event website: [全民資訊素養自我評量](https://isafeevent.moe.edu.tw/)
I don't know who are out of their minds think that doing 300 times on the same problems is called **learning**, so I made this tool to help myself, and also help the others.
But why I shared this on GitHub?
I do want to get the prizes, but I want to get it fairly.
When everyone hits the limit effortlessly, it becomes a lucky draw.
Anyways, good luck!

**WARNING: On [event info](https://isafeevent.moe.edu.tw/page/activity/), it doesn't mention using automatic tool is unacceptable, but rules can be changed.
Please follow up the rules before using it.**

## Installation

- Use pip to install selenium and dotenv.
- Typing these 2 commands on your terminal:

```bash
pip install selenium
```

```bash
pip install python-dotenv
```

- Copy this project to your local repository.
- Find `.env` file and modify the examples to match your email and password.
(You can register from [the website](https://isafeevent.moe.edu.tw/signin/))

## Usage

- Run `main.py`, after a while, a chrome browser should appear.
- Browser should redirect you to login page, since I don't know how to break captcha, type it yourself and click login button.
- After successfully login, the automatic submission process will get starting.
- During this process, DO NOT interfere it.
You can minimize it and it will run on background.
