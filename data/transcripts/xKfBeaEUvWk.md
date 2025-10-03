---
video_id: "xKfBeaEUvWk"
title: "Ask A Tailscale Engineer: What are ACL tags?"
description: "This video walks through ACLs tags in Tailscale, and details what is new with our ACL tag GA.

https://tailscale.com/blog/acl-tags-ga/..."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2022-02-01"
duration_seconds: 402
youtube_url: "https://www.youtube.com/watch?v=xKfBeaEUvWk"
thumbnail_url: "https://i.ytimg.com/vi/xKfBeaEUvWk/hqdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T17:48:36.184429"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 1227
transcription_time_seconds: 10.3
---

# Ask A Tailscale Engineer: What are ACL tags?

**[00:06](https://youtube.com/watch?v=xKfBeaEUvWk&t=6s)** Hi, I'm Maya Keterowski, a product manager here at Tailscale, and I'm here with MESM. Can you introduce yourself? Hi, I'm MESMOLI. I'm an engineer here at Tailscale. I've been here for 10 months. It looks like we're here to talk about ACLs today. Yeah, that's right. So first off, what are access control lists, which people sometimes call ACLs or ACLs? ACLs in the context of the ACLs, specify which of your devices can communicate with which of your other devices.

**[00:36](https://youtube.com/watch?v=xKfBeaEUvWk&t=36s)** So MESM's devices can talk to Maya's devices, or Maya's devices can only talk to Maya's devices. So how do I restrict it so that I can only talk to my own devices? So you would go to the admin console in Tailscale, and you would change the default allow policy to say that Maya's devices can talk to Maya's devices. We have docs on how to use the correct policy syntax. Got it. And the correct answer wrong, the policy is a default deny, so that unless I explicitly say something,

**[01:06](https://youtube.com/watch?v=xKfBeaEUvWk&t=66s)** the devices can't talk to each other. Great. Got it. Any other way I can update the ACLs other than in the admin console? So we also have an API so you can like fetch, update the ACLs programatically, if you want. Okay. So now that we know a bit more about ACLs, what are ACL tags? That's a great question. When I get my laptop to join a tailnet, it shows up in the admin console or in the tailnet as MESM's device, or like if you were to sign in on your phone, it will show up as Maya's device, right? Because you used your account

**[01:36](https://youtube.com/watch?v=xKfBeaEUvWk&t=96s)** to sign in. And that makes sense, right? I'm logging in on my laptop. It's identified as being my laptop, right? Great. Right. It makes sense. But then there are certain types of devices, like servers or shared internal analytics pipelines or whatever, in which they're not really tied tied to me. I might have worked on them when I was provisioning them initially, but they have nothing to do with me after that fact. Right. So they should not be tied to my identity. They should be tied. They should have their own permission model. And that's what ACL tags allows me to do.

**[02:07](https://youtube.com/watch?v=xKfBeaEUvWk&t=127s)** And so wager describing sounds a lot like something I've seen in other products called a service account, which was like a machine identity. How are accult tags different from service accounts. They are very similar, as you mentioned, they both apply to machines where there's no human associate with a service accounts live in your identity provider or they come from your identity provider. And you can only typically have one service account bird device. With ACL tags, you can actually have multiple tags for

**[02:37](https://youtube.com/watch?v=xKfBeaEUvWk&t=157s)** device. And that that allows you to do more flexible policies. Like in my person till that, I have like a policy, it says that infrastructure devices are in a device that are tagged with info can talk to all the devices that are tagged with info. But one of the infrared devices is also a DNS server. And I want all of my other talent devices to be able to talk to that on the DNS board. So I can like have multiple policies target the same node because of the way their tags are associated with that node.

**[03:07](https://youtube.com/watch?v=xKfBeaEUvWk&t=187s)** I love that you have an infratag in your personal talent.

**[03:11](https://youtube.com/watch?v=xKfBeaEUvWk&t=191s)** What happens if I have more than one tag, so like if I have something that's tagged both, you know, production and tag like Europe as an example.

**[03:19](https://youtube.com/watch?v=xKfBeaEUvWk&t=199s)** When the policy engine is evaluating policies, it does so independently. So if you have a device, if you have a policy for tag Europe, and you have a policy for tag broad, both of those would be applied to the

**[03:30](https://youtube.com/watch?v=xKfBeaEUvWk&t=210s)** device that has both of those tags. It is not that there's no intersection being applied here. It is always a union.

**[03:39](https://youtube.com/watch?v=xKfBeaEUvWk&t=219s)** So part of the reason we're talking today is that aquatags are becoming generally available, which is really exciting. What's new as part of the GA.

**[03:48](https://youtube.com/watch?v=xKfBeaEUvWk&t=228s)** We wanted to improve the user experience around tag notes in general. One of the biggest fake points was when a user who authenticated a tag node left a company, the tag node would also disappear with the user's account.

**[04:03](https://youtube.com/watch?v=xKfBeaEUvWk&t=243s)** This is something that we fix in the GA launch. So tag notes now stick around even if the user who authenticated them has left.

**[04:11](https://youtube.com/watch?v=xKfBeaEUvWk&t=251s)** And that makes sense, because before, you know, if you think about a laptop, right, if I leave, then you don't want my laptop on the tailman anymore, but you probably still want the server that I provision, because that's a shared resource.

**[04:21](https://youtube.com/watch?v=xKfBeaEUvWk&t=261s)** Exactly.

**[04:22](https://youtube.com/watch?v=xKfBeaEUvWk&t=262s)** Another thing that we added was the ability to have alt keys that are tagged.

**[04:27](https://youtube.com/watch?v=xKfBeaEUvWk&t=267s)** So let's talk about alt keys a bit. Alt keys are this concept in tail skill, which are keys are tokens that you can generate from the added panel or the API that allows you to

**[04:37](https://youtube.com/watch?v=xKfBeaEUvWk&t=277s)** provision tail and devices without going through the interactive process.

**[04:42](https://youtube.com/watch?v=xKfBeaEUvWk&t=282s)** So you don't have to like sit there and click a URL or open the URL and hit the link.

**[04:47](https://youtube.com/watch?v=xKfBeaEUvWk&t=287s)** Whenever those devices would come up previously, they would be associated with my identity. They would not be packed.

**[04:54](https://youtube.com/watch?v=xKfBeaEUvWk&t=294s)** But now you can specify a tag or an alt key. So whenever those devices originally come up in a tailnet, they're automatically associated with the tag.

**[05:02](https://youtube.com/watch?v=xKfBeaEUvWk&t=302s)** So they're not ever tied with my.

**[05:04](https://youtube.com/watch?v=xKfBeaEUvWk&t=304s)** Interesting. So when would I use an off key with an Apple tech?

**[05:08](https://youtube.com/watch?v=xKfBeaEUvWk&t=308s)** Journal of automation is something that comes up pretty frequently. One of the things that I want is the ability to, if I have a CIC pipeline, I want the ability to

**[05:18](https://youtube.com/watch?v=xKfBeaEUvWk&t=318s)** spin up new devices that are that are joined my tailwind. Right now I can give that that deployment script or pipeline, the hot key and whenever it spins up a new machine.

**[05:29](https://youtube.com/watch?v=xKfBeaEUvWk&t=329s)** That machine will join my tailwind as the desired tag.

**[05:32](https://youtube.com/watch?v=xKfBeaEUvWk&t=332s)** So it's already restricted when I joined the tailnet to whatever accles you have in place. That's pretty good. Yeah, it's pretty nice.

**[05:39](https://youtube.com/watch?v=xKfBeaEUvWk&t=339s)** Another thing that does come up with this same problem is now if I have to spin up like n types of machines, I either need n and alt keys or you can use this new concept that we where you can have a tag that can own other tags.

**[05:54](https://youtube.com/watch?v=xKfBeaEUvWk&t=354s)** So you can have a single auth key that is tagged with tag deployer or tax ccd and that can have access to like provision your property sources or provision your dev resources, whichever.

**[06:07](https://youtube.com/watch?v=xKfBeaEUvWk&t=367s)** So you can have a single auth key manage multiple tax.

**[06:10](https://youtube.com/watch?v=xKfBeaEUvWk&t=370s)** That means that so then rather than giving my deployment pipeline, you know, five different off keys, you know, one for prod and one for test and one for dev or whatever.

**[06:19](https://youtube.com/watch?v=xKfBeaEUvWk&t=379s)** I can just give it one off key and then give it the ability to tag things.

**[06:23](https://youtube.com/watch?v=xKfBeaEUvWk&t=383s)** That's cool. That's cool.

**[06:26](https://youtube.com/watch?v=xKfBeaEUvWk&t=386s)** Well, I learned a lot about accult tags today, very excited for the general availability. Thank you so much.

**[06:32](https://youtube.com/watch?v=xKfBeaEUvWk&t=392s)** Smith them. Thank you, Maya.

---

*Automatically generated transcript. May contain errors.*
