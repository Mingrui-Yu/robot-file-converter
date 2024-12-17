from converter_utils.utils_urdf import urdf_to_xml, create_rigid_object_mjcf



def test_urdf_to_mujoco_xml():
    urdf_path = "xxx.urdf"
    saved_xml_path = "xxx.xml"
    urdf_to_xml(urdf_path=urdf_path, saved_xml_path=saved_xml_path)


if __name__ == "__main__":
    test_urdf_to_mujoco_xml()