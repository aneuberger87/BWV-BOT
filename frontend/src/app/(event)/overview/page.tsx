import InputUploadBox from "@/components/custom/input-upload-box";

const Page = () => {
  return (
    <div className="flex flex-wrap gap-6">
      <InputUploadBox
        label="Schülerliste hochladen"
        description="Laden Sie die Schülerliste hoch"
        validateFunction={() => true}
        dataViewHref="/companies"
      />
      <InputUploadBox
        label="Firmenliste hochladen"
        description="Laden Sie die Firmenliste hoch"
        validateFunction={() => true}
        dataViewHref="/students"
      />
      <InputUploadBox
        label="Raumliste hochladen"
        description="Laden Sie die Raumliste hoch"
        validateFunction={() => false}
        dataViewHref="/rooms"
      />
    </div>
  );
};

export default Page;
