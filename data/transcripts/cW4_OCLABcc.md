---
video_id: "cW4_OCLABcc"
title: "Configuration Audit Logging"
description: "Maya Kaczorowski, Head of Product @ Tailscale walks through configuration audit logs which let you identify who did what, and when, in your tailnet...."
channel_name: "Tailscale"
channel_id: "UCcdv38QxPjSMqbt5ffLhJLA"
published_at: "2022-10-13"
duration_seconds: 143
youtube_url: "https://www.youtube.com/watch?v=cW4_OCLABcc"
thumbnail_url: "https://i.ytimg.com/vi/cW4_OCLABcc/maxresdefault.jpg"

# Transcription metadata
transcribed_at: "2025-10-03T18:08:35.756628"
transcription_method: "cpu"
model_used: "base"
language: "en"
word_count: 366
transcription_time_seconds: 3.3
---

# Configuration Audit Logging

**[00:00](https://youtube.com/watch?v=cW4_OCLABcc&t=0s)** Hi, I'm Maya Kajarowski, Product Manager here at Tailscale, and in this video, we're going to demo configuration audit logging. Configuration audit logs let you identify who did what and when in your tailnet. Configuration audit logs record actions that modify a tailnet's configuration. I already have a tailscale account, so let's go see what these logs look like. For each log, you'll see the type of action, the actor, the target resource, and the time in which these happened.

**[00:32](https://youtube.com/watch?v=cW4_OCLABcc&t=32s)** It's automatically enabled by default for all tailnets and cannot be disabled. Events are stored for 90 days. So, for example, if I create an auth key, and then, you know, I just show you all that auth key, so I'm going to delete it, then that'll show up in audit logs. In practice, events appear within seconds of them occurring. Or if I make a change to my tailnet policy file, then that change is noted in my configuration audit logs. Logs for changes to the tailnet

**[01:09](https://youtube.com/watch?v=cW4_OCLABcc&t=69s)** policy file include a diff between the previous and the new file. To find logs for a specific event, such as to verify that user was successfully onboarded, or to see if a user connected any suspicious activity during the time period, you can filter logs to the appropriate time period, type of event, actor, or search for target. For example, all search for all the events taken by Alice. Configuration audit logs are visible in the admin console by all admins of a tailnet, as well as you

**[01:40](https://youtube.com/watch?v=cW4_OCLABcc&t=100s)** users with the auditor role. Configuration audit logs are also available via API. You can export logs for a given time period, and store them elsewhere for long-term storage. Audit logs only include changes to my configuration. So, write changes to the coordination server. This doesn't include if someone access the tailnet to read your existing configuration, if a configuration was changed via support request, or information about connections within your tailnet. For the full list of events that are captured in configuration audit logs,

**[02:13](https://youtube.com/watch?v=cW4_OCLABcc&t=133s)** see the documentation. Now that you've seen how configuration audit logs work with tailscale, try it out yourself. Go to tailscale.com to get started.

---

*Automatically generated transcript. May contain errors.*
