class Solution:
    def uniqueEmailGroups(self, emails: list[str]) -> int:
        s = set()
        for email in emails:
            local_name, domain = email.split("@")
            local_name = local_name.replace(".", "").split("+")[0].lower()
            s.add((local_name, domain.lower()))
        return len(s)