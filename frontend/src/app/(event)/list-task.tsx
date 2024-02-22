import { Suspense } from "react";
import { getAllCompanies } from "../../lib/fetches";
import { FaCheck, FaExclamationTriangle, FaTimes, FaCog } from "react-icons/fa";

const StatusEmote = ({
  status,
}: {
  status: "done" | "pending" | "error" | "none";
}) => {
  switch (status) {
    case "done":
      return <FaCheck style={{ color: "green" }} />;
    case "pending":
      return <FaCog style={{ color: "grey" }} />;
    case "error":
      return <FaExclamationTriangle style={{ color: "orange" }} />;
    default:
      return <FaTimes style={{ color: "red" }} />;
  }
};

const ListTask = async () => {
  const data = await getAllCompanies();
  return (
    <div className="grid grid-cols-[auto_1fr] gap-2 items-center">
      {/* <div
        className="col-span-2 text-red-200 text-center bg-red-900
      "
      >
        ↓//TODO↓
      </div> */}
      <StatusEmote status="done" />
      <span>Schülerliste hochgeladen</span>
      <StatusEmote status="done" />
      <span>Schülerliste validiert</span>
      <div className="col-span-2"></div>
      <StatusEmote status="done" />
      <span>Firmenliste hochgeladen</span>
      <StatusEmote status="error" />
      <span>Firmenliste validiert</span>
      <div className="col-span-2"></div>
      <StatusEmote status="none" />
      <span>Raumliste hochgeladen</span>
      <StatusEmote status="none" />
      <span>Raumliste validiert</span>
    </div>
  );
};

const ListSuspense = () => {
  return (
    <Suspense fallback={<div>Loading</div>}>
      <ListTask />
    </Suspense>
  );
};

export default ListSuspense;
