---
video_id: "Xjo7_yHOTTA"
title: "Tailscale SSH Demo (90 seconds)"
description: "90-second demo of Tailscale SSH in beta.

https://tailscale.com/blog/tailscale-ssh/
https://tailscale.com/kb/1193/tailscale-ssh/..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2022-06-22"
duration_seconds: 95
youtube_url: "https://www.youtube.com/watch?v=Xjo7_yHOTTA"
thumbnail_url: "https://i.ytimg.com/vi/Xjo7_yHOTTA/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T17:53:07.624145"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 248
transcription_time_seconds: 2.4
---

# Tailscale SSH Demo (90 seconds)

**[00:00](https://youtube.com/watch?v=Xjo7_yHOTTA&t=0s)** Hi, I'm Maya from Tailscale, here to talk about Tailscale SSH. Tailscale SSH allows you to establish SSH connections between devices, as authorized by access controls, and authenticates and encrypts your SSH connection using WireGuard. To enable Tailscale SSH, you need to opt in the destination device to Tailscale SSH, and ensure ACLs exist which allow Tailscale SSH access. Your ACLs need two components. A regular access rule that allows a user to access the device on port 202.

**[00:30](https://youtube.com/watch?v=Xjo7_yHOTTA&t=30s)** And an SSH access rule that allows the user to use Tailscale SSH to access the device. You can also specify check rules to require users to re-authenticate before establishing high risk connections. The default ACLs in Tailscale allow users to SSH to their own devices using check mode. All right. On my server, I can advertise Tailscale SSH by running Tailscale up SSH. When you enable Tailscale SSH on a device, Tailscale claims port 222.

**[01:00](https://youtube.com/watch?v=Xjo7_yHOTTA&t=60s)** For any traffic, incoming to that device, to its Tailscale IP address, and the traffic is routed to an SSH server run by Tailscale, and the Steppever Standard SSH server. You can see it popped up in the admin panel. Then to connect, I can just SSH directly to the device. Since I have check mode enabled on this device, only to re-authenticate. And that's it. I'm in. By using Tailscale SSH, you no longer need to generate, distribute, and manage SSH keys or run a bastion.

**[01:32](https://youtube.com/watch?v=Xjo7_yHOTTA&t=92s)** Check out Tailscale.com to get started.

---

*Automatically generated transcript. May contain errors.*
