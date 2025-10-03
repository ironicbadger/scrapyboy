---
video_id: "k_MxlYIHAvI"
title: "MagicDNS"
description: "Member of Technical Staff, Charlotte Brandhorst-Satzkorn walks through how MagicDNS allows you to access devices on your Tailscale network with a human-readable name, rather than having to remember an..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2022-10-20"
duration_seconds: 106
youtube_url: "https://www.youtube.com/watch?v=k_MxlYIHAvI"
thumbnail_url: "https://i.ytimg.com/vi_webp/k_MxlYIHAvI/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T16:26:05.982049"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 325
transcription_time_seconds: 2.6
---

# MagicDNS

**[00:00](https://youtube.com/watch?v=k_MxlYIHAvI&t=0s)** Hi, I'm Charlotte Brandwith Satscon, member of Technical Staff here at Tailscale. Today, I'm going to share my few Magic DNS. Magic DNS allows you to access devices on your Tailscale network using a human readable name, rather than having to remember an IP address. Tailscale automatically assigns an IP address for every single unique device when you're telling it, giving you a stable IP that you can use to access the device no matter where it's located. With Magic DNS, your device's name is registered as a DNS entry.

**[00:30](https://youtube.com/watch?v=k_MxlYIHAvI&t=30s)** If you update your device's name, the Magic DNS entry will also automatically change. You can use the Magic DNS name to access the device. So, for example, as a Sage PyCrust, that works when you're on your townnet, but if you're accessing a device outside of your townnet, you'll also need to include the townnet name. Your townnet name is in the form of TailHex.TS.net, with a randomly generated hex. This unique name is what is used when registering DNS entries for Magic DNS. It is also used when sharing your device with another townnet

**[01:00](https://youtube.com/watch?v=k_MxlYIHAvI&t=60s)** and for issuing TLS certificates. You can change your townnet name to a fun name, which is at the form of something related to a tail and something related to a scale. So, when you want to access a shared device, Magic DNS uses the device name plus the townnet name. In this case, I could use the human readable name, such as chair.philosoreaptorjustice.TS.net. Magic DNS is enabled by default on all townnets created on or after October 20th, 2022. If your townnet does not have Magic DNS enabled,

**[01:30](https://youtube.com/watch?v=k_MxlYIHAvI&t=90s)** you can enable it by going to the admin console and going to the DNS settings. Now that you've seen how Magic DNS works in TailScale and how easy it is to access your device using a short name, give it a try yourself. Go to tailscales.com to get started.

---

*Automatically generated transcript. May contain errors.*
