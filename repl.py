from prompt_toolkit import CommandLineInterface, AbortAction, Exit
from prompt_toolkit.layout import Layout
from prompt_toolkit.line import Line
from prompt_toolkit.layout.prompt import DefaultPrompt
from prompt_toolkit.layout.menus import CompletionMenu
from prompt_toolkit.completion import Completion, Completer
from pygments.lexers import HyLexer
from hy.cmdline import HyREPL

class HyCompleter(Completer):
    keywords = HyLexer.special_forms + HyLexer.declarations + HyLexer.builtins

    def complete_after_insert_text(self, document):
        """
        Open completion menu when we type a character.
        (Except if we typed whitespace.)
        """
        return not document.char_before_cursor.isspace()

    def get_completions(self, document):
        word_before_cursor = document.get_word_before_cursor()

        for keyword in self.keywords:
            if keyword.startswith(word_before_cursor):
                yield Completion(keyword, -len(word_before_cursor))

def main():
    layout = Layout(before_input=DefaultPrompt('> '), lexer=HyLexer, menus=[CompletionMenu()])
    line = Line(completer=HyCompleter())
    cli = CommandLineInterface(layout=layout, line=line)
    try:
        repl = HyREPL()
        while True:
            code_obj = cli.read_input(on_exit=AbortAction.RAISE_EXCEPTION)
            repl.runsource(code_obj.text)
    except Exit:
        print 'GoodBye!'

if __name__ == '__main__':
    main()
