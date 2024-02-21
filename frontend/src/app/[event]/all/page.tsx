import FirmenUpload from "@/components/custom/firmen-upload";
import SchuelerUpload from "@/components/custom/schueler-upload";

const Page = () => {
  return (
    <div className="flex gap-6">
      <FirmenUpload />
      <SchuelerUpload />
    </div>
  );
};

export default Page;
