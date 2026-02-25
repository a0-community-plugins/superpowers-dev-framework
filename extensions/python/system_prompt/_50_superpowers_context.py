from python.helpers.extension import Extension


class SuperpowersContext(Extension):

    async def execute(self, system_prompt: list[str] = [], **kwargs):
        prompt = self.agent.read_prompt("fw.superpowers.reference.md")
        if prompt:
            system_prompt.append(prompt)
