# rootless_diff

This repo doesn't actually diff the files. It is simply a dumping ground so we can diff rootless files.

For example:

```bash
diff -u 10.12.3_16D32/com.apple.xpc.launchd.rootless.plist 10.12.4_16E195/com.apple.xpc.launchd.rootless.plist
```

Here you will notice Apple removed over 400 daemons from the `RemovableServices` dictionary with the point release of 10.12.4.

---

Pull requests accepted.
