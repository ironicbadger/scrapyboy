---
video_id: "lxE8a8gIA8c"
title: "Tailscale Network Flow Logs & Log Streaming Demo"
description: "Pouyan Aminian, Product Manager @ Tailscale walks through network flow logs and log streaming which helps you gain visibility into activity on your tailnet. 

Network flow logs blog post: https://tail..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2023-04-27"
duration_seconds: 242
youtube_url: "https://www.youtube.com/watch?v=lxE8a8gIA8c"
thumbnail_url: "https://i.ytimg.com/vi_webp/lxE8a8gIA8c/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T16:19:37.046216"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 760
transcription_time_seconds: 6.3
---

# Tailscale Network Flow Logs & Log Streaming Demo

**[00:00](https://youtube.com/watch?v=lxE8a8gIA8c&t=0s)** Hello, my name is Puyan, and I'm a product manager here at Tailscale. Today we're going

**[00:05](https://youtube.com/watch?v=lxE8a8gIA8c&t=5s)** to talk about a feature that we recently launched called network flow logging and log streaming.

**[00:11](https://youtube.com/watch?v=lxE8a8gIA8c&t=11s)** Now what is network flow logging? It is simply a log of activity that is happening across

**[00:16](https://youtube.com/watch?v=lxE8a8gIA8c&t=16s)** your tailnet. As a security administrator, chances are you would want to know this information

**[00:22](https://youtube.com/watch?v=lxE8a8gIA8c&t=22s)** in order to detect and mitigate threats, investigate security incidents, or simply make sure

**[00:27](https://youtube.com/watch?v=lxE8a8gIA8c&t=27s)** you're maintaining a good compliance posture. These logs include information such as which

**[00:31](https://youtube.com/watch?v=lxE8a8gIA8c&t=31s)** node is talking to which other node, how many packets are being transmitted, and what is

**[00:36](https://youtube.com/watch?v=lxE8a8gIA8c&t=36s)** the total number of bytes sent or received. All of these logs are associated with a time stamp

**[00:41](https://youtube.com/watch?v=lxE8a8gIA8c&t=41s)** and a node ID which will help you build time series or correlate the logs back to the specific

**[00:46](https://youtube.com/watch?v=lxE8a8gIA8c&t=46s)** device that is transmitting them. As always, it is important to note that we do not log

**[00:50](https://youtube.com/watch?v=lxE8a8gIA8c&t=50s)** nor do we have access to log the content of the packets that are transmitted across your

**[00:56](https://youtube.com/watch?v=lxE8a8gIA8c&t=56s)** tailnet. Next, we're going to do a quick demo on how you can set up and access network flow

**[01:00](https://youtube.com/watch?v=lxE8a8gIA8c&t=60s)** logs. To set them up, go to your admin console, go to the log step, go to the network flow logs

**[01:06](https://youtube.com/watch?v=lxE8a8gIA8c&t=66s)** up tab, and click start logging. And once you confirm this dialog, logs will flow. There are two

**[01:12](https://youtube.com/watch?v=lxE8a8gIA8c&t=72s)** ways that you can access these logs. You can either call this API, or you can stream these logs

**[01:17](https://youtube.com/watch?v=lxE8a8gIA8c&t=77s)** directly to a destination of your choice, which we'll talk about in a little bit.

**[01:22](https://youtube.com/watch?v=lxE8a8gIA8c&t=82s)** Now, in order to get these logs from our APIs, you need some piece of information, which you can

**[01:27](https://youtube.com/watch?v=lxE8a8gIA8c&t=87s)** find for the most part over here. First off, you need your tailnet ID, which you can find from here.

**[01:33](https://youtube.com/watch?v=lxE8a8gIA8c&t=93s)** Then, you're going to need to generate some keys that allow you access to the APIs. I've already

**[01:38](https://youtube.com/watch?v=lxE8a8gIA8c&t=98s)** created mine, so we're good to go. And finally, you need to specify a time window over which you want

**[01:43](https://youtube.com/watch?v=lxE8a8gIA8c&t=103s)** to search logs. Now, in the interest of time, I've already have a setup configured over here,

**[01:50](https://youtube.com/watch?v=lxE8a8gIA8c&t=110s)** which I'm just going to copy over. So here's my tailnet ID. Here's a start time,

**[01:59](https://youtube.com/watch?v=lxE8a8gIA8c&t=119s)** and finally, here's an end time. And by the way, these times are in UTC. For security reasons,

**[02:06](https://youtube.com/watch?v=lxE8a8gIA8c&t=126s)** I'm not going to copy over my access token, but you can do so in the similar manner.

**[02:13](https://youtube.com/watch?v=lxE8a8gIA8c&t=133s)** And once I have all this information in place, I run this command, and voila, logs are flowing.

**[02:22](https://youtube.com/watch?v=lxE8a8gIA8c&t=142s)** Now, as you can see, this data can get quite messy, and I don't think anybody finds a job of

**[02:27](https://youtube.com/watch?v=lxE8a8gIA8c&t=147s)** pulling an API to get results much fun, which is why we supported this notion of log streaming,

**[02:32](https://youtube.com/watch?v=lxE8a8gIA8c&t=152s)** which will allow you to send logs directly to a destination of your choice. As of this video,

**[02:38](https://youtube.com/watch?v=lxE8a8gIA8c&t=158s)** we support two destinations, Splunk, and Logstash, which is part of ELK. In order to set them up,

**[02:45](https://youtube.com/watch?v=lxE8a8gIA8c&t=165s)** again, you need some information, which you can obtain from these partners. In the case of Splunk,

**[02:50](https://youtube.com/watch?v=lxE8a8gIA8c&t=170s)** you need a URL and a token. And in the case of Logstash, you're going to need a URL, a username,

**[02:56](https://youtube.com/watch?v=lxE8a8gIA8c&t=176s)** and a token. In the interest of security, I will set this up offscreen, and I'll show you what

**[03:01](https://youtube.com/watch?v=lxE8a8gIA8c&t=181s)** the results look like in Logstash next. As promised, I configured my Logstash endpoint offscreen

**[03:06](https://youtube.com/watch?v=lxE8a8gIA8c&t=186s)** with a URL, a username, and a token. Let's switch over to the server to see what it looks like.

**[03:13](https://youtube.com/watch?v=lxE8a8gIA8c&t=193s)** So over here, we have the log of this little ping I did a while ago. This is a demo environment,

**[03:19](https://youtube.com/watch?v=lxE8a8gIA8c&t=199s)** so we don't have much going on over here. But you've access to do all the things that you normally

**[03:24](https://youtube.com/watch?v=lxE8a8gIA8c&t=204s)** would in Logstash, such as searching over logs with certain keywords, or selecting a custom time frame

**[03:31](https://youtube.com/watch?v=lxE8a8gIA8c&t=211s)** to zoom into. Network flow logs is available to all customers with a premium or enterprise plan.

**[03:37](https://youtube.com/watch?v=lxE8a8gIA8c&t=217s)** Log streaming is available on the enterprise plan only, and customers who are on that plan

**[03:42](https://youtube.com/watch?v=lxE8a8gIA8c&t=222s)** can use log streaming for configuration audit logs as well. Finally, I'd like to thank you for

**[03:46](https://youtube.com/watch?v=lxE8a8gIA8c&t=226s)** taking the time to watch this brief demo, and I hope you found it useful. If you have feedback

**[03:51](https://youtube.com/watch?v=lxE8a8gIA8c&t=231s)** for us, or if you have any questions, please feel free to reach out to us via the links provided in

**[03:56](https://youtube.com/watch?v=lxE8a8gIA8c&t=236s)** the description below. Thank you, and have a good rest of eating.

---

*Automatically generated transcript. May contain errors.*
