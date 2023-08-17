import React, { useState } from 'react'
import '../components/Formstyles.css'
import axios from 'axios'

export default function Form() {
    const[fname,setFname] = useState('');
    const[id,setId] = useState('');
    const[contact,setContact] = useState('');
  
    const[file,setFile]=useState('');
    const [uploadedFileURL, setUploadedFileURL] = useState(null)



    const handleRegister = async (e) => {
      e.preventDefault();
  
      const formData = new FormData();
      formData.append("fname", fname);
      formData.append("id", id);
      formData.append("contact", contact);
      formData.append("file",file)
      const url='http://localhost:5000/api/register'

      const config = {
        headers: {
          'content-type': 'multipart/form-data',
        },
      };

      axios.post(url, formData, config).then((response) => {
        setUploadedFileURL(response.data.fileUrl);
        console.log(uploadedFileURL)
      });
  

      console.log("Form Data:", formData);
  
   
  };

  return (
    <div>
        <form onSubmit={handleRegister}>
            <div className='first'>
                <label>Name</label>
                <input type='text' className='fname' onChange={(e)=> setFname(e.target.value)} required></input>
            </div>
            <br/>


            <div className='first'>
            <label>Employee ID</label>
                <input type='text' className='id' onChange={(e) => setId(e.target.value)} required></input>

            </div>
            <br/>

            <div className='first'>
            <label>Contact</label>
                <input type='int' className='contact' onChange={(e)=>setContact(e.target.value)} required></input>

            </div>
            <br/>
            <div className='first'>
            
                <input type='file'  onChange={(e)=>setFile(e.target.files[0])} required></input>

            </div>
            <br/>
        
            <div className='first'>
                <input type='submit' className='submit' required></input>

            </div>
            
            
            <div>
            {uploadedFileURL && <p>{uploadedFileURL}</p>}</div>
        </form>
      
    </div>
  )
}
