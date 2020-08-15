ClassicEditor
    .create(document.querySelector('#editor'), {
      toolbar: [ 'heading', '|', 'alignment', 'bold', 'italic', 'link', 'bulletedList', 'numberedList', 'blockQuote' ],
      heading: {
        options: [
          { model: 'paragraph', title: 'Paragraph', class: 'ck-heading_paragraph' },
          { model: 'heading1', view: 'h1', title: 'Heading 1', class: 'ck-heading_heading1' },
          { model: 'heading2', view: 'h2', title: 'Heading 2', class: 'ck-heading_heading2' }
        ]
      }
    })
    .then((editor) => {
      const toolbarContainer = document.querySelector('#toolbar-container')
      toolbarContainer.appendChild(editor.ui.view.toolbar.element)
    })
    .catch((error) => {
      console.error(error)
    })

  const button_upload = document.getElementById('button_upload')
  const input_file = document.getElementById('input_file')
  const image_container = document.getElementById('image_container')
  const image_wrapper = document.getElementsByClassName('image_container__wrapper')[0]
  const close_image = document.getElementsByClassName('close_image')[0]

  function readURL(input) {
    if (input.files && input.files[0]) {
      const reader = new FileReader()
      reader.onload = (e) => {
        image_container.src = e.target.result
        showImageWrapper(true)
      }
      reader.readAsDataURL(input.files[0])
    }
  }

  let showImageWrapper = (state) => {
    button_upload.hidden = state
    image_wrapper.hidden = !state
  }

  button_upload.onclick = function() {
    input_file.click()
  }

  input_file.oninput = function() {
    readURL(this)
  }

  close_image.onclick = function() {
    showImageWrapper(false)
  }
