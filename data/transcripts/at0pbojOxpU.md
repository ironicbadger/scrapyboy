---
video_id: "at0pbojOxpU"
title: "User & Group Provisioning for Okta in Tailscale Demo"
description: "A quick demo of User & Group Provisioning for Okta in Tailscale...."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2022-04-19"
duration_seconds: 158
youtube_url: "https://www.youtube.com/watch?v=at0pbojOxpU"
thumbnail_url: "https://i.ytimg.com/vi_webp/at0pbojOxpU/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T17:54:51.719904"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 382
transcription_time_seconds: 4.1
---

# User & Group Provisioning for Okta in Tailscale Demo

**[00:00](https://youtube.com/watch?v=at0pbojOxpU&t=0s)** Hi, I'm Ramiya Nagarajan, member of Technical Staff here at Tailscale. In this video, we're

**[00:06](https://youtube.com/watch?v=at0pbojOxpU&t=6s)** going to demo how to use Groups in Octa as part of ACLs in Tailscale. In Tailscale,

**[00:12](https://youtube.com/watch?v=at0pbojOxpU&t=12s)** ACLs or Access Control lists are how you define which devices can talk to other devices

**[00:17](https://youtube.com/watch?v=at0pbojOxpU&t=17s)** as part of your tailnet. If you have a set of users who all need access to the same resources,

**[00:23](https://youtube.com/watch?v=at0pbojOxpU&t=23s)** rather than listing each user explicitly in an ACL rule, you can define a group. In the

**[00:29](https://youtube.com/watch?v=at0pbojOxpU&t=29s)** ACL file, you can list which users are part of the group and then refer to that group in an

**[00:35](https://youtube.com/watch?v=at0pbojOxpU&t=35s)** ACL rule. Unfortunately, this is manual and doesn't necessarily reflect the latest changes in

**[00:41](https://youtube.com/watch?v=at0pbojOxpU&t=41s)** your organization, such as employees leaving or teams being reorganized. Instead, you can use

**[00:47](https://youtube.com/watch?v=at0pbojOxpU&t=47s)** user and group provisioning. With user and group provisioning, you can sync group membership

**[00:53](https://youtube.com/watch?v=at0pbojOxpU&t=53s)** that you define in your identity provider, such as Octa, for use in Tailscale ACLs. We'll talk

**[00:59](https://youtube.com/watch?v=at0pbojOxpU&t=59s)** through how to sync a group from Octa to Tailscale and update the ACL rule that we have here.

**[01:04](https://youtube.com/watch?v=at0pbojOxpU&t=64s)** Let's assume that we've already configured user and group provisioning for our Tailscale network

**[01:10](https://youtube.com/watch?v=at0pbojOxpU&t=70s)** to our Octa instance. However, you can see that we're not yet syncing any groups. In fact,

**[01:17](https://youtube.com/watch?v=at0pbojOxpU&t=77s)** in Octa, for the Tailscale application, we're not yet pushing any groups. In our ACLs, we've

**[01:24](https://youtube.com/watch?v=at0pbojOxpU&t=84s)** manually defined the group membership for the group engineering. But in Octa, there's already a

**[01:30](https://youtube.com/watch?v=at0pbojOxpU&t=90s)** group called engineering that reflects how our team is currently structured. These have the

**[01:36](https://youtube.com/watch?v=at0pbojOxpU&t=96s)** same users as what's defined in the Tailscale ACL. To make these groups accessible to Tailscale,

**[01:41](https://youtube.com/watch?v=at0pbojOxpU&t=101s)** in the Tailscale app and Octa, find group engineering and push it to Tailscale. And you see that it's

**[01:59](https://youtube.com/watch?v=at0pbojOxpU&t=119s)** already sent. To use the sync group in an ACL, copy the group from the sidebar and replace the

**[02:06](https://youtube.com/watch?v=at0pbojOxpU&t=126s)** previous manual group that we had defined in the ACL rule. And now we can delete the manually defined

**[02:16](https://youtube.com/watch?v=at0pbojOxpU&t=136s)** group. When a change in membership happens in Octa, this will be reflected in Tailscale automatically.

**[02:26](https://youtube.com/watch?v=at0pbojOxpU&t=146s)** User and group provisioning is available in Tailscale in the business plan. Now that you've

**[02:31](https://youtube.com/watch?v=at0pbojOxpU&t=151s)** seen how to use sync groups in Tailscale, trying to trade out yourself, check out Tailscale.com

**[02:37](https://youtube.com/watch?v=at0pbojOxpU&t=157s)** to get started.

---

*Automatically generated transcript. May contain errors.*
