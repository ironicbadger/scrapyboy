---
video_id: "t-iJq8jp6y0"
title: "Tailscale Up: Share Mount"
description: "This talk was given by Kevin Meziere at Tailscale Up in San Francisco on Wednesday, May 31, 2023...."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2023-07-07"
duration_seconds: 115
youtube_url: "https://www.youtube.com/watch?v=t-iJq8jp6y0"
thumbnail_url: "https://i.ytimg.com/vi_webp/t-iJq8jp6y0/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T15:58:20.869440"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 294
transcription_time_seconds: 2.8
---

# Tailscale Up: Share Mount

**[00:00](https://youtube.com/watch?v=t-iJq8jp6y0&t=0s)** Okay, so my name is Kevin. I'm with John Plain University in San Diego. We've been working on rolling out Tailscale slowly to our users. And one thing that we wanted to do was give them an easy way to mount shared folders that we provide them for different departments or whatever. It's kind of a pain to tell users, okay, you're going to go into finder, open and give them this long string or even worse, you know, open up terminal and run mount and all this garbage.

**[00:30](https://youtube.com/watch?v=t-iJq8jp6y0&t=30s)** We had this idea that with Tailscale, we could use the JSON CLI API and get some information on what drives people had access to from there. And then we would run that command on that user's computer.

**[00:50](https://youtube.com/watch?v=t-iJq8jp6y0&t=50s)** The interface that we had for that though was an MDM self-service app. And the problem with that was that we didn't get to give them a listing of particular drives. It was just kind of mount everything. And on top of that, it ended up running everything as root, which is less than ideal.

**[01:09](https://youtube.com/watch?v=t-iJq8jp6y0&t=69s)** So this is kind of like the gross command that we would have ran. And then we decided, oh, we can just make a little app that would run instead. So we have this thing here. And this goes through and at list, everything that has a or any of the end points that you can connect to that has a tag containing SMB in it. And we can just click it. And it's mounted now. And if you click it again, it'll open it up and it definitely connects up.

**[01:40](https://youtube.com/watch?v=t-iJq8jp6y0&t=100s)** So that's a share amount. And I thought we're going to get there you go. So yeah, so there you go.

---

*Automatically generated transcript. May contain errors.*
