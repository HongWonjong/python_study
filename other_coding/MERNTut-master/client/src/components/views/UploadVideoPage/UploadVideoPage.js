import React, { useState, useEffect } from "react";
import { Typography, Button, Form, message, Input, Icon } from "antd";
import Dropzone from "react-dropzone";

const { Title } = Typography;
const { TextArea } = Input;

function UploadVideoPage(props) {
  return (
    <div style={{ maxWidth: "700px", margin: "2rem auto" }}>
      <div style={{ textAlign: "center", marginBottom: "2rem" }}>
        <Title level={2}> Upload Video</Title>
      </div>

      <Form>
        <div style={{ display: "flex", justifyContent: "space-between" }}>
          <Dropzone onDrop={acceptedFiles => console.log(acceptedFiles)}>
            {({ getRootProps, getInputProps }) => (
              <section>
                <div {...getRootProps()}>
                  <input {...getInputProps()} />
                  <p>Drag 'n' drop some files here, or click to select files</p>
                </div>
              </section>
            )}
          </Dropzone>

          {/* {Thumbnail !== "" && (
            <div>
              <img src={`http://localhost:5000/${Thumbnail}`} alt="haha" />
            </div>
          )} */}
        </div>

        <br />
        <br />
        <label>Title</label>
        <Input
          // onChange={handleChangeTitle}
          // value={title}
        />
        <br />
        <br />
        <label>Description</label>
        <TextArea
          // onChange={handleChangeDecsription}
          //value={Description}
        />
        <br />
        <br />

        {/* <Button type="primary" size="large" onClick={onSubmit}>
          Submit
        </Button> */}
      </Form>
    </div>
  );
}

export default UploadVideoPage;
