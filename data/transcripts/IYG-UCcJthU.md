---
video_id: "IYG-UCcJthU"
title: "Tailscale Docker Desktop Extension"
description: "With the Tailscale Docker Desktop extension, you can use Tailscale to securely connect to the resources you need for development, including internal tools and databases, no matter where you are or whe..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2022-05-10"
duration_seconds: 220
youtube_url: "https://www.youtube.com/watch?v=IYG-UCcJthU"
thumbnail_url: "https://i.ytimg.com/vi/IYG-UCcJthU/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T18:10:16.251521"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 630
transcription_time_seconds: 5.8
---

# Tailscale Docker Desktop Extension

**[00:01](https://youtube.com/watch?v=IYG-UCcJthU&t=1s)** Hi, I'm Ross. I'm a designer and developer at Tailscale, and I'm here today to show the new Tailscale Docker Desktop extension. If you're not familiar with Tailscale, it's an easy way to create secure, private networks that connect different devices, no matter where they are. Even if there's firewalls or containerization layers between those devices, Tailscale gives every device a static IP address and a human readable DNS name that they can use to talk with each other. It's kind of like having your own personal land that works from anywhere. So the Tailscale Docker Desktop extension

**[00:32](https://youtube.com/watch?v=IYG-UCcJthU&t=32s)** extends that capability to your Docker containers. Any containers that expose public ports will be shared with your Tailscale private network. This makes it really easy to collaborate with your teammates on local dev servers or access remote containers via SSH. Maybe you've got a package server or a licensing server that needs to stay private.

**[00:52](https://youtube.com/watch?v=IYG-UCcJthU&t=52s)** Tailscale lets you access them without ever exposing anything to the public internet. The Tailscale Docker Desktop extension is available at the launch of the Docker Desktop extension marketplace. You can find it in the list and install it with a single click.

**[01:08](https://youtube.com/watch?v=IYG-UCcJthU&t=68s)** Once you've got it installed, you can start by logging in with your browser. Even if you don't have an account, this is the place to begin. The account you use to log in with will determine which Tailscale network your containers will be exposed to.

**[01:21](https://youtube.com/watch?v=IYG-UCcJthU&t=81s)** So I'll just get started with my personal network. Great. Once you're logged in, you'll see a list of all your containers that are exposing public ports. And alongside that, you'll see this Tailscale URL column. These URLs, these IP addresses, are 100.x.y.ziP addresses. They're private IP addresses that are static that Tailscale assigns each device.

**[01:44](https://youtube.com/watch?v=IYG-UCcJthU&t=104s)** You can use this IP address and share it with other people who are on your same Tailscale network, such as your colleagues. Your colleagues will be able to access your server, but nobody else around the world will. It's completely private.

**[01:56](https://youtube.com/watch?v=IYG-UCcJthU&t=116s)** So to demonstrate this, I'll open this up in my browser and it will fail to find it. That's because even though the Tailscale Docker Desktop extension is running Tailscale, my host machine isn't.

**[02:11](https://youtube.com/watch?v=IYG-UCcJthU&t=131s)** Now, if I connect to my Tailscale network via my host machine, and I try that URL again, great. There's my demo server. So IP addresses aren't the only way that you can access Tailscale resources.

**[02:26](https://youtube.com/watch?v=IYG-UCcJthU&t=146s)** We also offer an easy human readable DNS name system called Magic DNS. To access it, go to the admin console section in the Docker Desktop extension.

**[02:38](https://youtube.com/watch?v=IYG-UCcJthU&t=158s)** You'll see a view that includes a list of all your machines in your network. And from here, you can go to the DNS tab, enable Magic DNS, and when you return to the Docker Desktop extension, you'll have nice human readable URLs.

**[02:51](https://youtube.com/watch?v=IYG-UCcJthU&t=171s)** T-Bore is my current computer. The Docker Desktop means it's from the Docker Desktop extension. I can take the same Magic DNS URL, paste it into my browser, or share it with my colleagues, and access the same Dev Server from there.

**[03:05](https://youtube.com/watch?v=IYG-UCcJthU&t=185s)** So, as I said before, this Tailscale Docker Desktop extension is available from the launch of the Docker Desktop extension store. And it's available to all Tailscale users, including those on the free plan. There's no payment needed.

**[03:18](https://youtube.com/watch?v=IYG-UCcJthU&t=198s)** If you want more details about how to use Tailscale or Docker Desktop, you can read our docs, which include a guide on how to get set up.

**[03:26](https://youtube.com/watch?v=IYG-UCcJthU&t=206s)** And elsewhere in our docs, we have guides on how to integrate Tailscale with other different kinds of services, like Postgres databases or specific cloud providers.

**[03:35](https://youtube.com/watch?v=IYG-UCcJthU&t=215s)** If you find it helpful, and let us know if you have any questions. Thanks.

---

*Automatically generated transcript. May contain errors.*
