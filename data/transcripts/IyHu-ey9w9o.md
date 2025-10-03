---
video_id: "IyHu-ey9w9o"
title: "GitHub secret scanning now available for Tailscale secrets!"
description: "GitHub secret scanning now scans your source code, issues, pull requests, wikis, and other data for any Tailscale secrets. When a potential match is found, GitHub verifies the authenticity of the secr..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2025-01-29"
duration_seconds: 250
youtube_url: "https://www.youtube.com/watch?v=IyHu-ey9w9o"
thumbnail_url: "https://i.ytimg.com/vi/IyHu-ey9w9o/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T17:34:43.006092"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 745
transcription_time_seconds: 6.7
---

# GitHub secret scanning now available for Tailscale secrets!

**[00:00](https://youtube.com/watch?v=IyHu-ey9w9o&t=0s)** I think it's a right of passage for anybody that works in infrastructure that at some point you're going to leak some kind of an access token. Well, in today's video, I want to show you in real time how Tailscale's new partnership with GitHub will protect you from leaking sensitive Tailscale secrets on the public internet. The first thing I'm going to do is generate an off key and just show you this flow in real time. I'm not going to do anything special at all. I'm going to copy and paste this off key, which is basically like a password, a token,

**[00:31](https://youtube.com/watch?v=IyHu-ey9w9o&t=31s)** which you can use to authenticate to your Tailnet programmatically. So in this case, I'm going to paste it into a Docker container, which I would then use to authenticate this container to my Tailnet and then have in this case bezel hub, which is a monitoring thing. By the way, I made a video about that up here. That would authenticate bezel to my Tailnet, the same as a password would essentially.

**[00:54](https://youtube.com/watch?v=IyHu-ey9w9o&t=54s)** So what you can see here is I'm just going to commit a totally valid secret. And this is, as you saw in real time, a real secret. Now note down here, it says three recently invalidated off keys was doing some testing before I recorded. So three is the number. Okay. And in real time, I wanted to see what happens. I'm going to commit this change and then sink this change to GitHub.

**[01:17](https://youtube.com/watch?v=IyHu-ey9w9o&t=77s)** The change is now synced. I'm going to go back to my other window. And in the time it took me to alt tab from VS code back to the browser. GitHub has already scanned my repository and revoked that key in real time.

**[01:31](https://youtube.com/watch?v=IyHu-ey9w9o&t=91s)** So this monitoring applies to five different kinds of secrets. I have a list here API keys preauthentication keys, O off client secrets, SCIM keys and web hook keys. Now there'll be a link in the description down below to a blog post explaining all of the nitty gritty details of this stuff.

**[01:51](https://youtube.com/watch?v=IyHu-ey9w9o&t=111s)** This new partnership between GitHub and tailscale enable secret scanning by default for any public repo. However, if you would like to be notified about what's going on, you're going to need to enable a couple settings in the background for your GitHub repo.

**[02:06](https://youtube.com/watch?v=IyHu-ey9w9o&t=126s)** So most repos should have a security tab up here. If you click on that, obviously make sure you're logged in as the administrator for that GitHub repo.

**[02:15](https://youtube.com/watch?v=IyHu-ey9w9o&t=135s)** Then click on the button here that says set up code scanning. All you need to do after that is go through the relevant sections and look for secret scanning down here and click enable.

**[02:26](https://youtube.com/watch?v=IyHu-ey9w9o&t=146s)** This is not turning on secret scanning per se. This is just turning on notifications. So if you commit something, you'll get a notification up here in the secret scanning options here under vulnerability alerts.

**[02:39](https://youtube.com/watch?v=IyHu-ey9w9o&t=159s)** You'll also get an email as well to your registered email address, that kind of thing. So it's just worth noting that this is turned on by default for every public repo. But if you want notifications of your leaky credential habits, you want to turn it on as an admin for the GitHub repo itself.

**[02:56](https://youtube.com/watch?v=IyHu-ey9w9o&t=176s)** And that's pretty much all there is to know about it to be honest with you. Of course, the best way to protect all of your secrets is to not put them in GitHub in the first place.

**[03:07](https://youtube.com/watch?v=IyHu-ey9w9o&t=187s)** Find some encrypted method to store your secrets, whatever has you called vault. If you're doing it in business world, or you can even use bit warden to store secrets and copy and paste them in.

**[03:17](https://youtube.com/watch?v=IyHu-ey9w9o&t=197s)** Or you can use environment variables and docker has a bunch of secret management tools. There's all sorts of ways around storing secrets in plain text on your local system.

**[03:27](https://youtube.com/watch?v=IyHu-ey9w9o&t=207s)** But this just gives you a bit more security, this latest partnership between GitHub and tail scale in order that you won't leak secrets onto the public internet anymore. So that's about it for today. Super quick video. I know. But if you're interested in learning more about this kind of thing and some of the stuff you can do with tail scale about bringing it to work.

**[03:44](https://youtube.com/watch?v=IyHu-ey9w9o&t=224s)** We have a new page over at tailscale.com slash BTW. And until next time, thank you so much for watching. I've been Alex from tail scale.

---

*Automatically generated transcript. May contain errors.*
