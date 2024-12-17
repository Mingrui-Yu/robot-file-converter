from converter_utils.utils_urdf import urdf_to_xml, create_rigid_object_mjcf



def test_urdf_to_mujoco_xml():
    urdf_path = "/home/mingrui/Mingrui/research/project_IL_contact/mujoco_test/leaphand_tac3d_mujoco/leap_hand_custom_tac3d.urdf"
    saved_xml_path = "/home/mingrui/Mingrui/research/project_IL_contact/mujoco_test/leaphand_tac3d_mujoco/leap_hand_custom_tac3d.xml"
    urdf_to_xml(urdf_path=urdf_path, saved_xml_path=saved_xml_path)


if __name__ == "__main__":
    test_urdf_to_mujoco_xml()