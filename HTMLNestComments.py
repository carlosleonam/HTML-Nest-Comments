import sublime, sublime_plugin

class NestCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
      if region.empty():
        continue
      text = self.view.substr(region)
      fileExt = self.view.window().extract_variables()['file_extension']
      if 'php' in fileExt:
        if text.startswith("/*"):
          # print('Uncomment Please')
          text = text[2:]
          text = text[:-2]
          text = text.replace('<~?', '<?')
          text = text.replace('?~>', '?>')
          text = text.replace('/~*', '/*')
          text = text.replace('*~/', '*/')
          self.view.replace(edit, region, text)
        else:
          # print('Comment these nested comments')
          text = text.replace('<?', '<~?')
          text = text.replace('?>', '?~>')
          text = text.replace('/*', '/~*')
          text = text.replace('*/', '*~/')
          self.view.replace(edit, region, text)
          self.view.insert(edit, self.view.sel()[0].begin(), "/*")
          self.view.insert(edit, self.view.sel()[0].end(), "*/")
      elif 'css' in fileExt:
        if text.startswith("/*"):
          # print('Uncomment Please')
          text = text[2:]
          text = text[:-2]
          text = text.replace('<~?', '<?')
          text = text.replace('?~>', '?>')
          text = text.replace('/~*', '/*')
          text = text.replace('*~/', '*/')
          self.view.replace(edit, region, text)
        else:
          # print('Comment these nested comments')
          text = text.replace('<?', '<~?')
          text = text.replace('?>', '?~>')
          text = text.replace('/*', '/~*')
          text = text.replace('*/', '*~/')
          self.view.replace(edit, region, text)
          self.view.insert(edit, self.view.sel()[0].begin(), "/*")
          self.view.insert(edit, self.view.sel()[0].end(), "*/")
      elif 'js' in fileExt:
        if text.startswith("/*"):
          # print('Uncomment Please')
          text = text[2:]
          text = text[:-2]
          text = text.replace('<~?', '<?')
          text = text.replace('?~>', '?>')
          text = text.replace('/~*', '/*')
          text = text.replace('*~/', '*/')
          self.view.replace(edit, region, text)
        else:
          # print('Comment these nested comments')
          text = text.replace('<?', '<~?')
          text = text.replace('?>', '?~>')
          text = text.replace('/*', '/~*')
          text = text.replace('*/', '*~/')
          self.view.replace(edit, region, text)
          self.view.insert(edit, self.view.sel()[0].begin(), "/*")
          self.view.insert(edit, self.view.sel()[0].end(), "*/")
      # else:
      elif 'html' in fileExt:
        if text.startswith("<!--"):
          # print('Uncomment Please')
          text = text[4:]
          text = text[:-3]
          text = text.replace('<~?', '<?')
          text = text.replace('?~>', '?>')
          text = text.replace('<!~~', '<!--')
          text = text.replace('~~>', '-->')
          self.view.replace(edit, region, text)
        else:
          # print('Comment these nested comments')
          text = text.replace('<?', '<~?')
          text = text.replace('?>', '?~>')
          text = text.replace('<!--', '<!~~')
          text = text.replace('-->', '~~>')
          self.view.replace(edit, region, text)
          self.view.insert(edit, self.view.sel()[0].begin(), "<!--")
          self.view.insert(edit, self.view.sel()[0].end(), "-->")

#http://www.sublimetext.com/forum/viewtopic.php?f=6&t=10984
