---
video_id: "Ad7D2pkFNdA"
title: "Exit Nodes | Tailscale Explained"
description: "In our \"Tailscale Explained\" series we show you all you need to know to get started on a particular area or feature of Tailscale.

In today's video we cover Tailscale Exit Nodes.

===

ERRATA: \"Allow ..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2024-11-08"
duration_seconds: 388
youtube_url: "https://www.youtube.com/watch?v=Ad7D2pkFNdA"
thumbnail_url: "https://i.ytimg.com/vi_webp/Ad7D2pkFNdA/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T17:29:07.264309"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 1118
transcription_time_seconds: 10.5
---

# Exit Nodes | Tailscale Explained

**[00:00](https://youtube.com/watch?v=Ad7D2pkFNdA&t=0s)** Welcome into another episode of Tailscale Explained, I'm Alex. This is the playlist where we tell you everything you ever wanted to know about Tailscale, things like subnet routers, Tailscale SSH and ACLs. In today's video, we're going to cover exit nodes. Now, what is an exit node? Well, simply put, it's a way for you to route all of the traffic from your client device, like a phone or a laptop, and have it exit onto the public internet via Tailscale at a specific

**[00:30](https://youtube.com/watch?v=Ad7D2pkFNdA&t=30s)** geographic point on the internet. So let's say you want to do some online banking whilst you're on holiday, and this happened to me this summer actually, I wanted to access my US bank account whilst I was in England. However, my bank decided that accessing their banking app from another country was a huge security risk. So what I did was I flipped on the exit node functionality so that my phone sent all of its traffic over Tailscale as an exit node to this house here in North Carolina.

**[00:59](https://youtube.com/watch?v=Ad7D2pkFNdA&t=59s)** Suddenly, my bank had no idea that my traffic was any different than if I was physically in this building. You might be familiar with this concept from the more traditional privacy VPN, such as Mulvad, who we have a partnership with, by the way.

**[01:12](https://youtube.com/watch?v=Ad7D2pkFNdA&t=72s)** These privacy VPNs are very good at making you appear as if you're in a different physical geographic location for all sorts of interesting reasons. But Tailscale is about so much more than that. Yes, you can do that too and emulate that functionality with exit nodes.

**[01:28](https://youtube.com/watch?v=Ad7D2pkFNdA&t=88s)** But Tailscale is great for companies and self-hosters alike. So let's dig into exit nodes.

**[01:35](https://youtube.com/watch?v=Ad7D2pkFNdA&t=95s)** By default, Tailscale acts as an overlay network. It only routes traffic between devices running Tailscale and doesn't touch your public internet traffic, such as when you visit Google or Hacker News, for example.

**[01:48](https://youtube.com/watch?v=Ad7D2pkFNdA&t=108s)** The overlay network configuration is ideal for most people who need secure communication between sensitive devices, such as company servers or home computers, but don't need or want the extra layers of encryption or latency for their public internet connection.

**[02:03](https://youtube.com/watch?v=Ad7D2pkFNdA&t=123s)** But what about if you're on an untrusted Wi-Fi network, such as a coffee shop or perhaps something at an airport, or maybe you want to have a way to quickly test a different network's view of the world to see if it's your local DNS implementation playing up perhaps.

**[02:17](https://youtube.com/watch?v=Ad7D2pkFNdA&t=137s)** That's where an exit node really comes in handy. Setting one up is straightforward. Many devices can be used as exit nodes ranging from a Linux system to a Windows or Mac computer to an Apple TV. Yes, really an Apple TV.

**[02:32](https://youtube.com/watch?v=Ad7D2pkFNdA&t=152s)** If you're running a DIY firewall like OpenSense, you can even install Tailscale directly there and use that single device that's presumably already on all the time in your network as an exit node and subnet router as well.

**[02:45](https://youtube.com/watch?v=Ad7D2pkFNdA&t=165s)** Here's a card to the tailscale explains subnet router video for you. The type of device you pick as an exit node doesn't really matter too much.

**[02:53](https://youtube.com/watch?v=Ad7D2pkFNdA&t=173s)** They're all likely going to be fast enough and bottlenecked by your internet speed at the location of the exit node itself.

**[02:59](https://youtube.com/watch?v=Ad7D2pkFNdA&t=179s)** But my personal pick for an always on low power device that you could ask a friend or a relative to host for you with little to no first might be something like an Apple TV, which consumes less than one watt in standby mode.

**[03:12](https://youtube.com/watch?v=Ad7D2pkFNdA&t=192s)** And yes, exit node and subnet routing functionality still works in this low power sleep state or the humble raspberry pie.

**[03:23](https://youtube.com/watch?v=Ad7D2pkFNdA&t=203s)** You might also consider running tailscale on a cloud VPS somewhere like Hetzner or Linnode. You can do this to use it as an easy way to pick a different geographic location for your traffic. However, it comes with a potential downside.

**[03:36](https://youtube.com/watch?v=Ad7D2pkFNdA&t=216s)** Rooting consumer level traffic like browsing via a data center IP block because remember you will now appear as if you're sat inside that data center is that captures and things aren't used to seeing that type of traffic from a commercial IP block will get a bit upset with you.

**[03:52](https://youtube.com/watch?v=Ad7D2pkFNdA&t=232s)** So you're much more likely to get those annoying puzzles if you do this long term.

**[03:58](https://youtube.com/watch?v=Ad7D2pkFNdA&t=238s)** On Linux enabling exit node functionality is as simple as a tailscale set dash dash advertise exit node command on the CLI on mac and windows you can simply select to allow this node to act as an exit node from the client settings.

**[04:14](https://youtube.com/watch?v=Ad7D2pkFNdA&t=254s)** Now, you will need to manually approve each node that requests this functionality in your tailscale admin console. This only takes a couple of clicks, but if you'd like we can set up an ACL rules automatically approve exit node requests using the auto approvers features in your ACLs.

**[04:32](https://youtube.com/watch?v=Ad7D2pkFNdA&t=272s)** I'll put a snippet up on screen right now and as you can see it's just a couple of lines of code that you paste into your admin console.

**[04:40](https://youtube.com/watch?v=Ad7D2pkFNdA&t=280s)** The auto approver of a root or exit node can be a user's full login email address, a group name, an auto group or a tag owner.

**[04:50](https://youtube.com/watch?v=Ad7D2pkFNdA&t=290s)** Once configured anytime you turn on exit node functionality, it will automatically approve itself onto your tailnet.

**[04:57](https://youtube.com/watch?v=Ad7D2pkFNdA&t=297s)** One final configuration setting I'd like to touch on is the allow LAN access setting enabling this will allow direct access to your local network when routing traffic through an exit node.

**[05:09](https://youtube.com/watch?v=Ad7D2pkFNdA&t=309s)** In other words, the network the exit node is physically connected to will not be reachable by clients using this exit node unless you enable this feature.

**[05:18](https://youtube.com/watch?v=Ad7D2pkFNdA&t=318s)** It's very much the same idea as a subnet router only with a little less fine grained control. If you'd like to be explicit about what is or is not allowed, then you should turn on subnet routing for the specific subnet ranges you're interested in instead.

**[05:33](https://youtube.com/watch?v=Ad7D2pkFNdA&t=333s)** Now, before we get out of here, a couple of caveats. On Android, MacOS and Windows, the exit node feature is still undergoing performance optimization as it runs in user space.

**[05:44](https://youtube.com/watch?v=Ad7D2pkFNdA&t=344s)** If you'd like the absolute best experience, we recommend that you use Linux. It can be as a VM or on top of that Raspberry Pi sat in one of your drawers that you swore one day, you'd find a perfectly good use case for it.

**[05:57](https://youtube.com/watch?v=Ad7D2pkFNdA&t=357s)** Well, this may well be it. So I think that about covers exit nodes. Don't forget to check out the links in the description down below to all of our live streams and all of the other tailscale explained playlists.

**[06:08](https://youtube.com/watch?v=Ad7D2pkFNdA&t=368s)** As always, thank you so much for watching and until next time, I've been Alex from tailscale.

---

*Automatically generated transcript. May contain errors.*
