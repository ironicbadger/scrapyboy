---
video_id: "0Wz79I35cdg"
title: "Just In Time Access for your Tailnet | How do you secure access to your network resources?"
description: "Just-in-time network access is now generally available for Tailscale Enterprise users, providing an API-first native solution to enhance security by granting temporary, time-bound elevated access to c..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-05-09"
duration_seconds: 476
youtube_url: "https://www.youtube.com/watch?v=0Wz79I35cdg"
thumbnail_url: "https://i.ytimg.com/vi/0Wz79I35cdg/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T17:58:48.953725"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 1337
transcription_time_seconds: 12.9
---

# Just In Time Access for your Tailnet | How do you secure access to your network resources?

**[00:00](https://youtube.com/watch?v=0Wz79I35cdg&t=0s)** As a developer or infrastructure engineer, how many times have you faced this scenario where

**[00:04](https://youtube.com/watch?v=0Wz79I35cdg&t=4s)** you need temporary access to a production system, but your organization's access control

**[00:10](https://youtube.com/watch?v=0Wz79I35cdg&t=10s)** is all or nothing. You either have permanent access, permanently, creating security

**[00:15](https://youtube.com/watch?v=0Wz79I35cdg&t=15s)** risks, or no access at all which blocks your work. This is exactly the problem that Tailscales

**[00:21](https://youtube.com/watch?v=0Wz79I35cdg&t=21s)** knew just in time access feature souls. JIT, or just in time access, provides temporary

**[00:27](https://youtube.com/watch?v=0Wz79I35cdg&t=27s)** task-specific permissions to resources in your Tailscale network. We call that a tailnet.

**[00:33](https://youtube.com/watch?v=0Wz79I35cdg&t=33s)** Instead of permanent privileges, team members receive exactly what they need only for the

**[00:38](https://youtube.com/watch?v=0Wz79I35cdg&t=38s)** time required to complete their tasks, so when the time expires, access is automatically

**[00:44](https://youtube.com/watch?v=0Wz79I35cdg&t=44s)** revoked.

**[00:45](https://youtube.com/watch?v=0Wz79I35cdg&t=45s)** So, who is JIT access for? Well, we think it's perfect for DevOps teams managing production

**[00:51](https://youtube.com/watch?v=0Wz79I35cdg&t=51s)** infrastructure, security conscious organizations wanting to limit standing permissions and companies

**[00:56](https://youtube.com/watch?v=0Wz79I35cdg&t=56s)** with strict compliance requirements. It's also ideal for managing contractors or temporary

**[01:02](https://youtube.com/watch?v=0Wz79I35cdg&t=62s)** workers who need limited access or for protecting critical systems like Kubernetes clusters and

**[01:08](https://youtube.com/watch?v=0Wz79I35cdg&t=68s)** production databases. Essentially, if you have sensitive resources that should only be accessed

**[01:13](https://youtube.com/watch?v=0Wz79I35cdg&t=73s)** when necessary, JIT access provides the security controls you need while maintaining productivity.

**[01:20](https://youtube.com/watch?v=0Wz79I35cdg&t=80s)** At its core, JIT access temporarily modifies your Tailnet's access control lists or ACLs.

**[01:27](https://youtube.com/watch?v=0Wz79I35cdg&t=87s)** These policies define who can access what and are evaluated in real time when connections

**[01:31](https://youtube.com/watch?v=0Wz79I35cdg&t=91s)** are attempted. JIT evaluates multiple attributes when determining if a connection should be permitted.

**[01:36](https://youtube.com/watch?v=0Wz79I35cdg&t=96s)** Things like device posture, software versions, and geographic locations are all checked

**[01:41](https://youtube.com/watch?v=0Wz79I35cdg&t=101s)** in real time against policy. These policy modifications though aren't permanent. They only exist

**[01:46](https://youtube.com/watch?v=0Wz79I35cdg&t=106s)** for the duration of the window of time that you request. So, let's say, for example,

**[01:50](https://youtube.com/watch?v=0Wz79I35cdg&t=110s)** you've got a maintenance window, that connection will only be permitted by the JIT access rules

**[01:56](https://youtube.com/watch?v=0Wz79I35cdg&t=116s)** during that specific timeframe. This works because Tailscales control plane dynamically evaluates

**[02:01](https://youtube.com/watch?v=0Wz79I35cdg&t=121s)** each connection based on your baseline access rules, plus any active JIT attributes for

**[02:06](https://youtube.com/watch?v=0Wz79I35cdg&t=126s)** a specific device. The result is that policies adapt to the specific moment they're needed.

**[02:12](https://youtube.com/watch?v=0Wz79I35cdg&t=132s)** Tailscales JIT access management is only available on our enterprise plan, but if you're interested

**[02:18](https://youtube.com/watch?v=0Wz79I35cdg&t=138s)** in implementing JIT, you can visit Tailscale.com slash sales and have one of our team reach out

**[02:23](https://youtube.com/watch?v=0Wz79I35cdg&t=143s)** to you to help you to discuss your needs. Well, I'm joined by Alan, who's one of our solutions

**[02:27](https://youtube.com/watch?v=0Wz79I35cdg&t=147s)** engineers here at Tailscale. He is our resident JIT expert and I've rigged him up to do

**[02:32](https://youtube.com/watch?v=0Wz79I35cdg&t=152s)** us a quick demo of JIT today. Thank you, Alex. And today, what we're going

**[02:37](https://youtube.com/watch?v=0Wz79I35cdg&t=157s)** to showcase the Tailscale Justin Time demo using Slack. This is available on GitHub and open

**[02:45](https://youtube.com/watch?v=0Wz79I35cdg&t=165s)** source for you to utilize. So in this case, let me kind of walk you through. I've got an admin

**[02:51](https://youtube.com/watch?v=0Wz79I35cdg&t=171s)** page here with my one user signed into my telnet. My client is signed in here as my client that

**[02:58](https://youtube.com/watch?v=0Wz79I35cdg&t=178s)** I'm going to demo access with. And you can see I have a page here called Demo Streamer that shows me

**[03:03](https://youtube.com/watch?v=0Wz79I35cdg&t=183s)** as not connected. So it says, sorry, Alan, you're on the tailnet, but you don't have access to

**[03:09](https://youtube.com/watch?v=0Wz79I35cdg&t=189s)** this device itself. And I can verify that by looking at my client, my tailscale status. You notice

**[03:16](https://youtube.com/watch?v=0Wz79I35cdg&t=196s)** there is no server named Demo Streamer or anything along that line. And I can even look at my client

**[03:23](https://youtube.com/watch?v=0Wz79I35cdg&t=203s)** here and look at network devices. And it does not show up here. I do have app connectors and exit

**[03:29](https://youtube.com/watch?v=0Wz79I35cdg&t=209s)** nodes, subnet routers, because those are in our demo environment set up for everybody to utilize.

**[03:35](https://youtube.com/watch?v=0Wz79I35cdg&t=215s)** So now I'm, you know, I'm Alan at Outlook and I need access to this production server to do some

**[03:40](https://youtube.com/watch?v=0Wz79I35cdg&t=220s)** work. So I'm going to ask my boss Alex over here to approve this. But first of all, I need to

**[03:45](https://youtube.com/watch?v=0Wz79I35cdg&t=225s)** fire off a workflow. So with the Slack integration, I'm going to fire it off. It's going to open up a

**[03:52](https://youtube.com/watch?v=0Wz79I35cdg&t=232s)** pop up here in a minute. And I'm going to choose the just in time tailscale demo system.

**[03:59](https://youtube.com/watch?v=0Wz79I35cdg&t=239s)** I'm going to choose which device takes a little bit. This is my MacBook today that I'm going to

**[04:04](https://youtube.com/watch?v=0Wz79I35cdg&t=244s)** sign in as for five minutes. And I'm going to have my boss, Mr. Alex, approve it. Need to

**[04:11](https://youtube.com/watch?v=0Wz79I35cdg&t=251s)** trouble shoot something. So I'm going to fire off a message. Now Alex is going to get a notification

**[04:19](https://youtube.com/watch?v=0Wz79I35cdg&t=259s)** on your side of Slack. Yep. I see that come in right away. So if I go down to this app down here,

**[04:25](https://youtube.com/watch?v=0Wz79I35cdg&t=265s)** get to tailscale access bot, you can see I've got the tag being requested by Alan, the user

**[04:31](https://youtube.com/watch?v=0Wz79I35cdg&t=271s)** is requesting a five minute access to the resource Allen V Outlook MacBook Pro.ts just works.net.

**[04:37](https://youtube.com/watch?v=0Wz79I35cdg&t=277s)** So I'm going to click on the big green approve button. And hopefully you'll see that come through.

**[04:42](https://youtube.com/watch?v=0Wz79I35cdg&t=282s)** There it is. Alan's request has approved. And I can verify this with the tailscale configuration

**[04:48](https://youtube.com/watch?v=0Wz79I35cdg&t=288s)** logs. Oh, and look, traffic is starting to flow on the right hand side. So now as an end user,

**[04:54](https://youtube.com/watch?v=0Wz79I35cdg&t=294s)** nothing I really had to do. I just requested temporary access. Tailscale logs that you can see here

**[05:00](https://youtube.com/watch?v=0Wz79I35cdg&t=300s)** where it makes an update using that was from our earlier one. Our node attributes and says,

**[05:05](https://youtube.com/watch?v=0Wz79I35cdg&t=305s)** hey, let's give Alan access. From a command line, I now see this new device called demo streamer.

**[05:13](https://youtube.com/watch?v=0Wz79I35cdg&t=313s)** I'm able to connect to it. And I can even SSH into this box or access it based on whatever tailscale

**[05:21](https://youtube.com/watch?v=0Wz79I35cdg&t=321s)** ACLs. In this instance, I have it set up to access all the ports. But in your environment,

**[05:27](https://youtube.com/watch?v=0Wz79I35cdg&t=327s)** you can set up saying, hey, we only want to allow access to a web based app, a web port,

**[05:32](https://youtube.com/watch?v=0Wz79I35cdg&t=332s)** 8443, or maybe SSH or any other custom port along that line. And a cool thing about this within

**[05:39](https://youtube.com/watch?v=0Wz79I35cdg&t=339s)** five minutes, this access will automatically be revoked, nothing I have to do. So if you have

**[05:44](https://youtube.com/watch?v=0Wz79I35cdg&t=344s)** this integrated in a ticketing system or want to grant somebody that just in time access quickly,

**[05:50](https://youtube.com/watch?v=0Wz79I35cdg&t=350s)** this is how one way that you can do that for sure. Tailscale provides several ways to implement

**[05:55](https://youtube.com/watch?v=0Wz79I35cdg&t=355s)** JIT access. The first, as I mentioned, are device posture attributes. These are key value pairs

**[06:00](https://youtube.com/watch?v=0Wz79I35cdg&t=360s)** attached to devices that can be used within your talent policy to determine access permissions.

**[06:06](https://youtube.com/watch?v=0Wz79I35cdg&t=366s)** Third party integrations are also another option as well. So tailscale partners with companies

**[06:10](https://youtube.com/watch?v=0Wz79I35cdg&t=370s)** like Slack, GitHub, Opal, Conductal One and SIM to provide seamless JIT access as well.

**[06:17](https://youtube.com/watch?v=0Wz79I35cdg&t=377s)** Tailscale also has a very well-featured API. So if you want to write a custom implementation

**[06:21](https://youtube.com/watch?v=0Wz79I35cdg&t=381s)** for your business, you can use the tailscale API to programmatically manage

**[06:25](https://youtube.com/watch?v=0Wz79I35cdg&t=385s)** policy files for JIT access. And finally, we also do group membership syncing as well. So you can

**[06:30](https://youtube.com/watch?v=0Wz79I35cdg&t=390s)** manage access based on group membership by syncing groups from your identity provider directly

**[06:35](https://youtube.com/watch?v=0Wz79I35cdg&t=395s)** to tailscale. All of these approaches work with your access control policies to provide the

**[06:40](https://youtube.com/watch?v=0Wz79I35cdg&t=400s)** right level of access for the right duration. Here are some of the key benefits of JIT access.

**[06:45](https://youtube.com/watch?v=0Wz79I35cdg&t=405s)** You can secure temporary access by granting users task specific permissions for only the

**[06:49](https://youtube.com/watch?v=0Wz79I35cdg&t=409s)** required duration of the task they need to complete. You can also protect critical production

**[06:54](https://youtube.com/watch?v=0Wz79I35cdg&t=414s)** infrastructure, including individual machines, groups of machines using tags and Kubernetes

**[06:59](https://youtube.com/watch?v=0Wz79I35cdg&t=419s)** clusters as well using our tailscale Kubernetes operator. You can also leverage seamless

**[07:03](https://youtube.com/watch?v=0Wz79I35cdg&t=423s)** automation by integrating with tools like Slack and GitHub actions or dedicated access management

**[07:09](https://youtube.com/watch?v=0Wz79I35cdg&t=429s)** platforms as well. So as we've seen, tailscale's JIT access provides a powerful yet user-friendly

**[07:15](https://youtube.com/watch?v=0Wz79I35cdg&t=435s)** way to securely manage access to your most critical resources. By placing standing permissions

**[07:20](https://youtube.com/watch?v=0Wz79I35cdg&t=440s)** with temporary task specific access, you can dramatically improve your security posture while

**[07:26](https://youtube.com/watch?v=0Wz79I35cdg&t=446s)** maintaining productivity. If you'd like to find out more about how you can bring tailscale to work,

**[07:31](https://youtube.com/watch?v=0Wz79I35cdg&t=451s)** then head on over to tailscale.com slash BTW and join over 10,000 other paying companies who have

**[07:37](https://youtube.com/watch?v=0Wz79I35cdg&t=457s)** already made the switch to tailscale. As always, thank you so much for watching and until next time,

**[07:42](https://youtube.com/watch?v=0Wz79I35cdg&t=462s)** I've been Alex from tailscale.

---

*Automatically generated transcript. May contain errors.*
