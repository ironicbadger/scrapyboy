---
video_id: "40AXZUN6c_8"
title: "Tailscale Up: Network Engineering Goes DevOopsie"
description: "This talk was given by Marino Wijay at Tailscale Up in San Francisco on Wednesday, May 31, 2023...."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2023-07-07"
duration_seconds: 342
youtube_url: "https://www.youtube.com/watch?v=40AXZUN6c_8"
thumbnail_url: "https://i.ytimg.com/vi_webp/40AXZUN6c_8/maxresdefault.webp"

# Transcription metadata
transcribed_at: "2025-10-03T18:22:49.563586"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 997
transcription_time_seconds: 8.6
---

# Tailscale Up: Network Engineering Goes DevOopsie

**[00:00](https://youtube.com/watch?v=40AXZUN6c_8&t=0s)** All right. Well, I don't need to introduce the title of my talk because Jeremy already did it for me, but welcome, welcome, everyone. Welcome to Tailscale up. I am going to take us back in time a little bit to when VPN technologies were really cool. And you might have heard that ServiceMesh is a VPN. Actually, I said that because I think of ServiceMesh is a VPN primarily because of some of the patterns that it's picked up over the years from things like IPsack VPNs and SSL VPNs and even overlay technologies.

**[00:30](https://youtube.com/watch?v=40AXZUN6c_8&t=30s)** My name is Marina, I am a platform slash developer advocate at Solo, do a number of things with the community enough about me. Do you need to network everything? Do you network everything? Why? Yes, of course we do. I mean, there are a lot of different endpoints, devices, environments that we have to sit there and think about networking. But how is the question? So, I want you all to imagine an OSI model for a second. Actually, I won't do that to you because I actually do have an OSI model for you. And I want you to just think about a stack that you would deploy

**[01:01](https://youtube.com/watch?v=40AXZUN6c_8&t=61s)** for, let's say Kubernetes. What would you pick as the right set of solutions to be able to enable a network? Well, in my case, we've got Kubernetes and Tailscale offering up some connectivity and compute. And you've got Sillium that offers up that strong container networking capability and also some additional features. And then you have Istio that provides the mesh layer. But wait, if we have two VPNs running, what does that actually mean? All right, let's go back in time. Where were you, where were you when I needed you get? Like Git is probably one of the most

**[01:31](https://youtube.com/watch?v=40AXZUN6c_8&t=91s)** valuable tools that we use today, right? In version control and the way we build our applications and deploy them and deploy the production. But many, many years ago, the first crime that I used to commit was storing all my configurations on my laptop, in Notepad, not uploading them to any server. And then realizing, you know, five minutes before that code over that I'm supposed to do that my system is no longer available. I've lost all my configs and then building everything on the fly. Big crime number one. The second crime number one.

**[02:01](https://youtube.com/watch?v=40AXZUN6c_8&t=121s)** The first crime that I used to commit was, hey, let's sweep a bunch of these networking problems under the rug. And let's just use SDN to solve that problem, where we just layer networks on top of networks. But today, we've gotten way past that. And we can actually codify a lot of our networking information in a variety of different layers, right? You could yaml your BGP all the way through. You could configure your container networking interface. You can configure your cloud environments in any way, shape, or form. And then policies follow with,

**[02:31](https://youtube.com/watch?v=40AXZUN6c_8&t=151s)** the yaml as well. But what does that mean for the right networking stack? Well, that could mean anything, because the networking stack can be comprised of a variety of different tools that you pick from the cloud native or extended ecosystem. In my case, I chose TailScale to provide baseline connectivity across different environments. I chose Kubernetes because it provides connectivity and compute services. And then you have Silium and Istio. Because when you think about that full stack, it completes the entire picture. And then you start using other services as you need to.

**[03:01](https://youtube.com/watch?v=40AXZUN6c_8&t=181s)** But wait, why is service mesh a VPN? How many of you have ever played with the sidecar before in Istio? So what does that sidecar actually do? It's actually proxying connections on behalf of that service, right? So when you take away the sidecar and you enter this world of ambient mesh, which is a sidecarless model, what happens to those functions? They have to move to proxies that live at the node level. Now, what is this resemble of VPN-like setup? Because these proxies

**[03:31](https://youtube.com/watch?v=40AXZUN6c_8&t=211s)** have to tunnel to other proxies for services to communicate. Now, when we get super complex, we start thinking about edge, cloud, data center, all these different environments, and we need to tie them all together. You might think, hey, how do I do this? Can I do this with just standard networking? No. You might need TailScale to provide that connectivity, but you also might need other services like Istio, Silium, and your cross-cloud DCIs that might exist to be able to make this possible. But when we start thinking about

**[04:01](https://youtube.com/watch?v=40AXZUN6c_8&t=241s)** VPNs for a second, there are two layers of VPNs we are playing in, and I call this VPNception. So let me just recite a quick poem that I used chatGPT to help me write. So, in the realms of zeros and ones where data rivers glide across the digital landscape where information tides collide, two sentinels rise known far and wide. TailScale at the base in Istio high and stride. TailScale the foundations solid and profound.

**[04:30](https://youtube.com/watch?v=40AXZUN6c_8&t=270s)** Safe guards are networked in a secure surround. And we as a mesh network in binary lace using public ease for identity setting a steady pace. Tunnel secure reliable crafted with precision through the thickest firewalls it maintains its mission. Traffic concealed and shielded out of sight across the internet's expanse throughout the darkest night.

**[04:55](https://youtube.com/watch?v=40AXZUN6c_8&t=295s)** Then comes Istio, layer high in supreme, a beacon in the world of microservices, a remarkable regime. With its service mesh at firmly controls regulating traffic flow, achieving lofty goals, from balancing workloads to failure recovery Istio's reign, secure robust and steadfast it sustains.

**[05:16](https://youtube.com/watch?v=40AXZUN6c_8&t=316s)** Observability and routing refine tools in line in Kubernetes Dominion Istio truly does shine. Stack they stand a mighty configuration, tailScale in Istio, a splendid orchestration, the lower and higher layers together they twine in the vast cyber sea where the data streams align. Thank you.

---

*Automatically generated transcript. May contain errors.*
