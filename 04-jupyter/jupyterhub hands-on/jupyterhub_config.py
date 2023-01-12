from dockerspawner import DockerSpawner
#c.JupyterHub.spawner_class = 'dockerspawner.SystemUserSpawner'

class DockerFormSpawner(DockerSpawner):

    def _options_form_default(self):
        return '''
		<label for="profile">Select a job profile:</label>
        <select class="form-control" name="profile" required="" autofocus="">
			<option value="jupyter/minimal-notebook" selected="">minimal</option>
			<option value="<enter here>">my notebook</option>
			<option value="custom">Custom Notebook</option>
        </select>
        <span id='custom'>
            <label for="customimagename">Enter an image name:</label>
            <input type=text name='customimagename' class='form-control' />
        </span>
        <script>
        if (document.getElementById('spawn_form').profile.value !='custom')
        {{
           document.getElementById('custom').style.display = "none"
        }}

        $('#spawn_form').find('[name=profile]').change(function(e)
            {{
              if (e.currentTarget.value == 'custom'){{$('#custom').show()}}
              else {{$('#custom').hide()}}
            }}
        )
        </script>
        <label for="cpu"> Enter number of CPU cores:</label>
        <input type=text name='cpu' class='form-control' />
        <label for="ram"> Enter required amount of RAM (In GB): </label>
        <input type=text name='ram' class='form-control' />
		'''

    def options_from_form(self, formdata):
        options = {}
        options['cimage'] = formdata.get('profile')[0].strip()
        if options['cimage'] == 'custom':
            options['cimage'] = formdata.get('customimagename')[0].strip()

        options['cpu'] = formdata.get('cpu', [''])[0].strip()
        options['ram'] = formdata.get('ram', [''])[0].strip()
 
        return options

    @property
    def image(self):
        if self.user_options.get('cimage'):
            image = self.user_options['cimage']
        else:
            image = 'jupyter/minimal-notebook'
        return image

    @property
    def cpu_guarantee(self):
        cpu = '1.0'
        if self.user_options.get('cpu'):
            cpu = self.user_options['cpu']
        return cpu

    @property
    def mem_guarantee(self):
        mem = '1Gi'
        if self.user_options.get('ram'):
            mem = self.user_options['ram'] + 'Gi'
        return mem


c.JupyterHub.spawner_class = DockerFormSpawner
c.DockerSpawner.host_ip = "0.0.0.0"
c.Authenticator.admin_users = { 'admin' }
c.JupyterHub.hub_ip = "0.0.0.0"
c.DockerSpawner.network_name = 'jupyterhub'