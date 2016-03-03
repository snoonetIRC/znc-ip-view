import znc
import collections

class userips(znc.Module):
    module_types = [znc.CModInfo.GlobalModule]
    description = "Shows IP addresses of connected users"

    def WebRequiresAdmin(self):
        return True

    def GetWebMenuTitle(self):
        return "User IPs"

    def OnWebRequest(self, sock, page, tmpl):

        users = znc.CZNC.Get().GetUserMap()
        ordered_users = collections.OrderedDict(sorted(users.items()))

        for user in ordered_users.items():
            row = tmpl.AddRow("UserLoop")
            row["User"] = user[0]

            user_clients = user[1].GetAllClients()
            ip_string = ''
            for client in user_clients:
                ip_string += client.GetRemoteIP() + ' '

            row["IP"] = ip_string

        return True
