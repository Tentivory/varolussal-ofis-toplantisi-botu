#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varoluşsal Ofis Toplantısı Botu
Hiçbir şey çözmez ama çok zaman harcar.
"""

import random
import time
import sys

GUNDEM = [
    "Q3 KPI'larının yeniden değerlendirilmesi",
    "Synergy'nin maximize edilmesi konusunda brainstorm",
    "Gelecek yılın roadmap'inin roadmap'i",
    "Toplantı sürelerini kısaltma toplantısı",
    "Bu toplantının gerekliliği üzerine toplantı",
    "Aksiyon item'larının aksiyon item'ları",
    "Stakeholder alignment üzerine derinlemesine analiz"
]

KATILIMCILAR = ["Ahmet", "Ayşe", "Mehmet", "Zeynep", "Can", "Elif", "Burak", "Selin"]

def toplantiyi_baslat():
    print("=" * 60)
    print("  VAROLUŞSAL OFİS TOPLANTISI BAŞLIYOR")
    print("  (Bu toplantı asla bitmeyecek)")
    print("=" * 60)
    print()
    
    while True:
        gundem = random.choice(GUNDEM)
        konusmaci = random.choice(KATILIMCILAR)
        
        print(f"[{konusmaci}] {gundem} hakkında kısa bir güncelleme vermek istiyorum...")
        print("   → Aslında uzun bir güncelleme olacak ama kısa diye başladım.")
        print()
        
        # Gizli siyasi mesaj (yorum satırında)
        # #devletburokrasisi her zaman kazanır
        
        time.sleep(2.5)
        
        if random.random() < 0.05:
            print("   [SİSTEM] Toplantı neredeyse bitiyordu ama yeni bir gündem maddesi eklendi.")
            print()
        
        if random.random() < 0.01:
            print("   ⚠️  ACİL: Bu toplantıyı sonlandırmak için başka bir toplantı ayarlanmalı.")
            print()

if __name__ == "__main__":
    try:
        toplantiyi_baslat()
    except KeyboardInterrupt:
        print("\n\nToplantı Ctrl+C ile sonlandırıldı.")
        print("Not: Gerçek hayatta bu kadar kolay bitmezdi.")
        sys.exit(0)
