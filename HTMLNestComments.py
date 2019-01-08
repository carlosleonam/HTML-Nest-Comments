import sublime, sublime_plugin

class NestCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
      if region.empty():
        continue
      text = self.view.substr(region)
      fileExt = self.view.window().extract_variables()['file_extension']
      current_scope = self.view.scope_name(self.view.sel()[0].b) # embedding.php text.html.basic
      print (current_scope)
      # elif (current_scope == 'embedding.php text.html.basic'):
      # print (current_scope == 'embedding.php text.html.basic')
      # print ('embedding.php text.html.basic' in current_scope)
      # print ('embedding.php' in current_scope)
      # print ('text.html.basic' in current_scope)

      strange_scope = 'text.html.basic source.js.embedded.html source.js meta.block.js meta.conditional.js meta.block.js'
      strange_scope_php = 'embedding.php text.html.basic meta.embedded.block.php source.php meta.function.php meta.block.php'
      strange_scope_js = 'text.html.basic source.js.embedded.html source.js meta.block.js meta.object-literal.js meta.object-literal.js'
      strange_scope_css = 'text.html.basic source.css.embedded.html source.css'

      if (((strange_scope in current_scope) and ('html' in fileExt) and ('source.php' not in current_scope)) or
         ((strange_scope_php in current_scope) and ('php' in fileExt)) or
         ((strange_scope_js in current_scope) and ('html' in fileExt)) or
         ((strange_scope_css in current_scope) and ('html' in fileExt)) ):
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


      elif ('embedding.php text.html.basic' in current_scope) and ('php' in fileExt) and ('source.php' not in current_scope):
      # elif (current_scope == 'embedding.php text.html.basic'):
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
      elif ('php' in fileExt) or ('class.php' in fileExt):
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
      else:
        if text.startswith("/*"):
          # print('Uncomment Please')
          text = text[2:]
          text = text[:-2]
          # text = text.replace('<~?', '<?')
          # text = text.replace('?~>', '?>')
          text = text.replace('/~*', '/*')
          text = text.replace('*~/', '*/')
          self.view.replace(edit, region, text)
        else:
          # print('Comment these nested comments')
          # text = text.replace('<?', '<~?')
          # text = text.replace('?>', '?~>')
          text = text.replace('/*', '/~*')
          text = text.replace('*/', '*~/')
          self.view.replace(edit, region, text)
          self.view.insert(edit, self.view.sel()[0].begin(), "/*")
          self.view.insert(edit, self.view.sel()[0].end(), "*/")

#http://www.sublimetext.com/forum/viewtopic.php?f=6&t=10984