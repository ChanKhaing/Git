



#  Linux LVM (Logical Volume Management) Hands-On Guide

This documentation covers the core concepts, practical setup, file system behavior, and expansion procedures for **LVM in Rocky Linux / RHEL**.

---

##  1. LVM Core Architecture (သဘောတရား အနှစ်ချုပ်)

```
[ Physical Disks (/dev/vdb, /dev/vdc) ]
                  │
                  ▼  (pvcreate)
        [ Physical Volumes (PV) ]
                  │
                  ▼  (vgcreate)
        [ Volume Group (VG: datavg) ]  <-- Storage Pool ကြီး
                  │
                  ▼  (lvcreate)
       [ Logical Volume (LV: data1) ]  <-- Virtual Partition
                  │
                  ▼  (mkfs.xfs / mkfs.ext4)
            [ File System ]
                  │
                  ▼  (mount)
         [ Directory (/mnt/data1) ]

```

---

## 🛠️ 2. Step-by-Step LVM Configuration

### Step 1: Disk စစ်ဆေးခြင်း

```bash
lsblk

```

> `/dev/vdb` (10G) နဲ့ `/dev/vdc` (10G) raw disk ၂ လုံး ရှိမရှိ စစ်သည်။

### Step 2: Physical Volume (PV) ဖန်တီးခြင်း

Disks တွေကို LVM စနစ်ထဲ သုံးနိုင်အောင် PV အဖြစ် ပြောင်းသည်။

```bash
sudo pvcreate /dev/vdb /dev/vdc
sudo pvs # စစ်ဆေးရန်

```

### Step 3: Volume Group (VG) ဖန်တီးခြင်း

PV ၂ လုံးကို ပေါင်းပြီး **`datavg`** ဆိုသော 20GB Storage Pool ကြီး ဆောက်သည်။

```bash
sudo vgcreate datavg /dev/vdb /dev/vdc
sudo vgs # စစ်ဆေးရန်

```

### Step 4: Logical Volume (LV) ခွဲထုတ်ခြင်း

`datavg` ထဲကနေ **`6GB`** ရှိသော **`data1`** ဆိုသည့် LV ခွဲထုတ်သည်။

```bash
# Syntax: sudo lvcreate -L <Size> -n <LV_Name> <VG_Name>
sudo lvcreate -L 6G -n data1 datavg
sudo lvs # စစ်ဆေးရန်

```

### Step 5: Format ချခြင်း (File System) & Mount လုပ်ခြင်း

Linux စနစ်မှ စာဖတ်/စာရေး လုပ်နိုင်ရန် Format ချပြီး Folder ထဲ ချိတ်ဆက်ပေးရသည်။

```bash
# XFS File System Format ချခြင်း
sudo mkfs.xfs /dev/datavg/data1

# Mount လုပ်မည့် Target Folder ဆောက်ခြင်း
sudo mkdir -p /mnt/data1

# Mount လုပ်ခြင်း
sudo mount /dev/datavg/data1 /mnt/data1

# Mount ဖြစ်မဖြစ် စစ်ဆေးခြင်း
df -h /mnt/data1

```

---

## ⚡ 3. Storage Expansion (Data မပျက်ဘဲ Size တိုးနည်း)

Volume Size ပြည့်သွားပါက Server Reboot ကျစရာမလိုဘဲ Online တိုးနိုင်သည်။

```bash
# 1. LV Size ကို 1GB ထပ်တိုးခြင်း (6GB -> 7GB)
sudo lvextend -L +1G /dev/datavg/data1

# 2. XFS File System ပါ Size လိုက်တိုးအောင် Stretch လုပ်ခြင်း
sudo xfs_growfs /mnt/data1

# စစ်ဆေးရန်
df -h /mnt/data1

```

---

## !!! 4. Key Learnings & Important Notes (အရေးကြီး အချက်များ)

### 1️⃣ XFS vs EXT4 File System ကွာခြားချက်

* **XFS (Default in RHEL/Rocky):**
* Size ထပ်တိုးခြင်း (`lvextend` + `xfs_growfs`) **ရသည်။**
* Size ပြန်လျှော့ခြင်း (Shrink/Reduce) **လုံးဝ မရပါ။**


* **EXT4:**
* Size တိုးခြင်းရော၊ လျှော့ခြင်းပါ **ရသည်။** (`lvreduce` + `resize2fs` သုံးရသည်)။



### 2️⃣ Devil's Advocate Review (သတိထားရန် အချက်များ)

* **Non-persistent Mount:** `mount` command ဖြင့် ချိတ်ထားသည်မှာ RAM ထဲတွင်သာ ရှိသေးသဖြင့် Server Reboot ကျပါက Mount ပြုတ်သွားမည်။ (Auto-mount ရန် `/etc/fstab` ထဲ ထည့်ရန်လိုသည်)။
* **No Redundancy:** Disks များကို RAID / Mirroring မပါဘဲ ဒီအတိုင်း ပေါင်းထားသဖြင့် Disk ၁ လုံး ပျက်ပါက VG တစ်ခုလုံး Data ပျက်စီးနိုင်သည်။

---

### 📝 Quick Command Cheat Sheet

| Action        |  PV Command | VG Command | LV Command |
| ---           | ---     --- | --- ------ |
| **Create**    | `pvcreate`  | `vgcreate` | `lvcreate` |
| **Display **  | `pvs`       | `vgs`      | `lvs`      |
| **Display D*  | `pvdisplay` | `vgdisplay`| `lvdisplay`|
| Extend Size| -| `vgextend`  | `lvextend` |

---