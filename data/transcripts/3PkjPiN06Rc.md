---
video_id: "3PkjPiN06Rc"
title: "Tailscale SSH Console"
description: "Head of Product Maya Kaczorowski walks us through how to use Tailscale SSH Console. Tailscale SSH Console allows you to initiate a browser-based Tailscale SSH session that connects directly from the w..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2022-10-27"
duration_seconds: 137
youtube_url: "https://www.youtube.com/watch?v=3PkjPiN06Rc"
thumbnail_url: "https://i.ytimg.com/vi_webp/3PkjPiN06Rc/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T16:10:42.231856"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 351
transcription_time_seconds: 3.2
---

# Tailscale SSH Console

**[00:00](https://youtube.com/watch?v=3PkjPiN06Rc&t=0s)** Hi, I'm Maya Katrovsky, head of product at Tailscale. In this video, we're going to demo Tailscale SSH Console. Tailscale SSH Console allows you to initiate a browser-based Tailscale SSH session that connects directly from the web-based admin console to a node on your tailnet. If you're not familiar with Tailscale SSH, it's a way to SSH to devices in your tailnet using Tailscale for authentication instead of managing SSH keys. If you've opted a device in to use Tailscale SSH,

**[00:31](https://youtube.com/watch?v=3PkjPiN06Rc&t=31s)** then you can use Tailscale SSH Console to access the device from the admin console. This is only possible if SSH access rules allow you to access the device and if you're in a minute the tailnet. To connect, select SSH on the device. Then select the username you'll connect as on the device. This list of user names is automatically populated from the users you've specified in the tailnet policy file or you can type in a username. Click SSH and reauthenticate.

**[01:03](https://youtube.com/watch?v=3PkjPiN06Rc&t=63s)** This will open a Tailscale SSH Console session in a new window. When you use Tailscale SSH Console, a Tailscale client starts running in your browser using web assembly and authenticates to your tailnet as an ephemeral node. This means that your browser joins your tailnet and just like other connections in Tailscale, traffic is end and encrypted from your browser to the node that you're connecting to.

**[01:30](https://youtube.com/watch?v=3PkjPiN06Rc&t=90s)** And we have a shell just like any other shell. The browser window corresponds to a single SSH session. If you want to connect multiple devices using console, the same session will be used. If you close the window, the session will automatically terminate and the node will automatically be removed from your tailnet. You can use Tailscale SSH Console to connect your devices in an emergency like when you're on call and don't have access to devices already running Tailscale.

**[02:02](https://youtube.com/watch?v=3PkjPiN06Rc&t=122s)** Now that you've seen how to use Tailscale SSH Console to connect and get a shell to devices in your tailnet, try it yourself. Tailscale SSH Console is now available in beta. Go to Tailscale.com to get started.

---

*Automatically generated transcript. May contain errors.*
